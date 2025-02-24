<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import { Image, StaticImage } from "@gradio/image";
	import { Block } from "@gradio/atoms";
	import { _ } from "svelte-i18n";
	import { Component as StatusTracker } from "../StatusTracker/";
	import type { LoadingStatus } from "../StatusTracker/types";
	import type { Styles } from "@gradio/utils";
	import UploadText from "../UploadText.svelte";

	export let elem_id: string = "";
	export let visible: boolean = true;
	export let value: null | string = null;
	export let source: "canvas" | "webcam" | "upload" = "upload";
	export let tool: "editor" | "select" = "editor";
	export let label: string;
	export let show_label: boolean;
	export let streaming: boolean;
	export let pending: boolean;
	export let style: Styles = {};
	export let mirror_webcam: boolean;
	export let shape: [number, number];
	export let brush_radius: number;

	export let loading_status: LoadingStatus;

	export let mode: "static" | "dynamic";

	const dispatch = createEventDispatcher<{ change: undefined }>();

	$: value, dispatch("change");
	let dragging: boolean;

	$: value = !value ? null : value;
</script>

<Block
	{visible}
	variant={mode === "dynamic" && value === null && source === "upload"
		? "dashed"
		: "solid"}
	border_mode={dragging ? "focus" : "base"}
	padding={false}
	{elem_id}
	style={{ height: style.height, width: style.width }}
	allow_overflow={false}
>
	<StatusTracker {...loading_status} />
	{#if mode === "static"}
		<StaticImage {value} {label} {show_label} />
	{:else}
		<Image
			{brush_radius}
			{shape}
			bind:value
			{source}
			{tool}
			on:edit
			on:clear
			on:change
			on:stream
			on:drag={({ detail }) => (dragging = detail)}
			on:upload
			on:error={({ detail }) => {
				loading_status = loading_status || {};
				loading_status.status = "error";
				loading_status.message = detail;
			}}
			{label}
			{show_label}
			{pending}
			{streaming}
			{mirror_webcam}
		>
			<UploadText type="image" />
		</Image>
	{/if}
</Block>
