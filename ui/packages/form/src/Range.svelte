<script context="module">
	let _id = 0;
</script>

<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import { BlockTitle } from "@gradio/atoms";

	export let value: number = 0;
	export let minimum: number = 0;
	export let maximum: number = 100;
	export let step: number = 1;
	export let disabled: boolean = false;
	export let label: string;
	export let info: string | undefined = undefined;
	export let show_label: boolean;

	const id = `range_id_${_id++}`;
	const dispatch = createEventDispatcher<{ change: number; release: number }>();

	function handle_release(e: MouseEvent) {
		dispatch("release", value);
	}

	$: dispatch("change", value);
	const clamp = () => {
		value = Math.min(Math.max(value, minimum), maximum);
	};
</script>

<div class="wrap">
	<div class="head">
		<label for={id}>
			<BlockTitle {show_label} {info}>{label}</BlockTitle>
		</label>
		<input
			type="number"
			bind:value
			min={minimum}
			max={maximum}
			on:blur={clamp}
			{step}
			{disabled}
		/>
	</div>
</div>

<input
	type="range"
	{id}
	name="cowbell"
	bind:value
	min={minimum}
	max={maximum}
	{step}
	{disabled}
	on:mouseup={handle_release}
/>

<style>
	.wrap {
		display: flex;
		flex-direction: column;
		width: 100%;
	}

	.head {
		display: flex;
		justify-content: space-between;
	}
	input[type="number"] {
		display: block;
		position: relative;
		outline: none !important;
		box-shadow: var(--input-shadow);
		border: var(--input-border-width) solid var(--input-border-color);
		border-radius: var(--input-radius);
		background: var(--input-background);
		padding: var(--size-2) var(--size-2);
		height: var(--size-6);
		color: var(--body-text-color);
		font-size: var(--input-text-size);
		line-height: var(--line-sm);
		text-align: center;
	}

	input[type="number"]:focus {
		box-shadow: var(--input-shadow-focus);
		border-color: var(--input-border-color-focus);
	}

	input::placeholder {
		color: var(--input-placeholder-color);
	}

	input[type="range"] {
		width: 100%;
		accent-color: var(--slider-color);
	}

	input[disabled] {
		cursor: not-allowed;
	}
</style>
