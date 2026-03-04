<script lang="ts">
	import type { Gradio } from "@gradio/utils";

	export let value: any;
	let old_value: any;
	export let gradio: Gradio<{
		change: never;
	}>;

	$: {
		if (value !== old_value) {
			old_value = value;
			gradio.dispatch("change");
		}
	}
</script>
