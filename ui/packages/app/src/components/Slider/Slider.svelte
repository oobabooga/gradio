<script lang="ts">
	import { Range } from "@gradio/form";
	import { Block } from "@gradio/atoms";
	import StatusTracker from "../StatusTracker/StatusTracker.svelte";
	import type { LoadingStatus } from "../StatusTracker/types";
	import type { Styles } from "@gradio/utils";

	export let elem_id: string = "";
	export let visible: boolean = true;
	export let value: number = 0;
	export let label: string = "Slider";
	export let info: string | undefined = undefined;
	export let style: Styles = {};
	export let minimum: number;
	export let maximum: number;
	export let step: number;
	export let mode: "static" | "dynamic";
	export let show_label: boolean;

	export let loading_status: LoadingStatus;
</script>

<Block
	{visible}
	{elem_id}
	disable={typeof style.container === "boolean" && !style.container}
>
	<StatusTracker {...loading_status} />

	<Range
		bind:value
		{label}
		{info}
		{show_label}
		{minimum}
		{maximum}
		{step}
		disabled={mode === "static"}
		on:change
		on:release
	/>
</Block>
