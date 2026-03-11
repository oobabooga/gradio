<svelte:options accessors={true} />

<script lang="ts">
	import type { Gradio } from "@gradio/utils";
	import { Block } from "@gradio/atoms";
	import { StatusTracker } from "@gradio/statustracker";
	import type { LoadingStatus } from "@gradio/statustracker";
	import DragDropList from "./shared/DragDropList.svelte";

	export let gradio: Gradio<{
		change: string;
		input: never;
		clear_status: LoadingStatus;
	}>;
	export let label = "DragDrop";
	export let info: string | undefined = undefined;
	export let elem_id = "";
	export let elem_classes: string[] = [];
	export let visible = true;
	export let value = "";
	export let container = true;
	export let scale: number | null = null;
	export let min_width: number | undefined = undefined;
	export let show_label: boolean;
	export let loading_status: LoadingStatus | undefined = undefined;
	export let interactive: boolean;
</script>

<Block
	{visible}
	{elem_id}
	{elem_classes}
	{scale}
	{min_width}
	allow_overflow={false}
	padding={container}
>
	{#if loading_status}
		<StatusTracker
			autoscroll={gradio.autoscroll}
			i18n={gradio.i18n}
			{...loading_status}
			on:clear_status={() => gradio.dispatch("clear_status", loading_status)}
		/>
	{/if}

	<DragDropList
		bind:value
		{label}
		{info}
		{show_label}
		{container}
		disabled={!interactive}
		on:change={() => gradio.dispatch("change", value)}
		on:input={() => gradio.dispatch("input")}
	/>
</Block>
