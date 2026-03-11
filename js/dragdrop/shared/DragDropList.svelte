<script lang="ts">
	import { createEventDispatcher, tick } from "svelte";
	import { BlockTitle } from "@gradio/atoms";

	export let value = "";
	export let label: string;
	export let info: string | undefined = undefined;
	export let show_label = true;
	export let container = true;
	export let disabled = false;

	const dispatch = createEventDispatcher<{
		change: string;
		input: undefined;
	}>();

	let items: string[] = [];
	let dragging_index: number | null = null;
	let drop_target: number | null = null;
	let list_el: HTMLDivElement;

	function parse_value(val: string): string[] {
		if (!val || !val.trim()) return [];
		return val
			.replace(/\n/g, ",")
			.split(",")
			.map((s) => s.trim())
			.filter((s) => s.length > 0);
	}

	function serialize_items(arr: string[]): string {
		return arr.join("\n");
	}

	$: {
		const parsed = parse_value(value);
		const current = serialize_items(items);
		const incoming = serialize_items(parsed);
		if (current !== incoming) {
			items = parsed;
		}
	}

	function handle_drag_start(e: DragEvent, index: number): void {
		if (disabled) return;
		dragging_index = index;
		if (e.dataTransfer) {
			e.dataTransfer.effectAllowed = "move";
			e.dataTransfer.setData("text/plain", String(index));
		}
	}

	function get_nearest_index(y: number): number {
		const children = Array.from(list_el.children) as HTMLElement[];
		for (let i = 0; i < children.length; i++) {
			const rect = children[i].getBoundingClientRect();
			const mid = rect.top + rect.height / 2;
			if (y < mid) return i;
		}
		return children.length - 1;
	}

	function handle_list_drag_over(e: DragEvent): void {
		if (disabled || dragging_index === null) return;
		e.preventDefault();
		if (e.dataTransfer) {
			e.dataTransfer.dropEffect = "move";
		}
		drop_target = get_nearest_index(e.clientY);
	}

	function handle_list_drag_leave(e: DragEvent): void {
		if (!list_el.contains(e.relatedTarget as Node)) {
			drop_target = null;
		}
	}

	function handle_list_drop(e: DragEvent): void {
		if (disabled || dragging_index === null) return;
		e.preventDefault();

		const target_index = drop_target;
		drop_target = null;

		if (target_index === null || dragging_index === target_index) {
			dragging_index = null;
			return;
		}

		const new_items = [...items];
		const [moved] = new_items.splice(dragging_index, 1);
		new_items.splice(target_index, 0, moved);

		items = new_items;
		dragging_index = null;

		value = serialize_items(items);
		tick().then(() => {
			dispatch("change", value);
			dispatch("input");
		});
	}

	function handle_drag_end(): void {
		dragging_index = null;
		drop_target = null;
	}
</script>

<label class:container>
	<BlockTitle {show_label} {info}>{label}</BlockTitle>

	<div
		class="drag-drop-list"
		class:disabled
		bind:this={list_el}
		on:dragover={handle_list_drag_over}
		on:dragleave={handle_list_drag_leave}
		on:drop={handle_list_drop}
	>
		{#each items as item, index (item + "-" + index)}
			<div
				class="drag-item"
				class:dragging={dragging_index === index}
				class:drag-over={drop_target === index && dragging_index !== index}
				draggable={!disabled}
				role="listitem"
				tabindex="0"
				on:dragstart={(e) => handle_drag_start(e, index)}
				on:dragend={handle_drag_end}
			>
				<span class="drag-handle">⠿</span>
				<span class="drag-label">{item}</span>
			</div>
		{/each}
	</div>
</label>

<style>
	label {
		display: block;
		width: 100%;
	}

	.drag-drop-list {
		display: flex;
		flex-direction: column;
		gap: 4px;
		padding: var(--input-padding);
		background: var(--input-background-fill);
		border-radius: var(--input-radius);
		max-height: 350px;
		overflow-y: auto;
	}

	.container > .drag-drop-list {
		border: var(--input-border-width) solid var(--input-border-color);
	}

	.drag-item {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 6px 10px;
		border-radius: var(--radius-sm, 4px);
		background: var(--block-background-fill);
		border: 1px solid var(--border-color-primary);
		color: var(--body-text-color);
		font-size: var(--input-text-size);
		font-weight: var(--input-text-weight);
		cursor: grab;
		user-select: none;
		transition: border-color 0.15s ease, background 0.15s ease;
	}

	.drag-item:active {
		cursor: grabbing;
	}

	.drag-item:hover {
		border-color: var(--input-border-color-focus);
	}

	.drag-item.dragging {
		opacity: 0.4;
	}

	.drag-item.drag-over {
		border-color: var(--color-accent);
		border-style: dashed;
		background: var(--input-background-fill);
	}

	.disabled .drag-item {
		cursor: default;
		opacity: 0.7;
	}

	.drag-handle {
		color: var(--body-text-color-subdued);
		font-size: var(--input-text-size);
		line-height: 1;
		flex-shrink: 0;
	}

	.drag-label {
		flex: 1;
		overflow: hidden;
		text-overflow: ellipsis;
		white-space: nowrap;
	}
</style>
