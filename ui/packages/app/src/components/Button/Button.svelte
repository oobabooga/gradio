<script lang="ts">
	import type { Styles } from "@gradio/utils";
	import { Button } from "@gradio/button";
	import { _ } from "svelte-i18n";

	export let style: Styles = {};
	export let elem_id: string = "";
	export let visible: boolean = true;
	export let value: string;
	export let variant: "primary" | "secondary" | "stop" = "secondary";
	export let mode: "static" | "dynamic" = "dynamic";
</script>

<Button
	{variant}
	{elem_id}
	{style}
	{visible}
	disabled={mode === "static"}
	on:click
>
	{$_(value)}
</Button>
