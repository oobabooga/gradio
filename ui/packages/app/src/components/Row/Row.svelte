<script lang="ts">
	import type { Styles } from "@gradio/utils";

	export let style: Styles = {};
	export let elem_id: string;
	export let visible: boolean = true;
	export let variant: "default" | "panel" | "compact" = "default";
</script>

<div
	class="flex"
	class:compact={variant === "compact"}
	class:panel={variant === "panel"}
	class:unequal-height={style.equal_height === false}
	class:stretch={style.equal_height}
	class:hide={!visible}
	id={elem_id}
>
	<slot />
</div>

<style>
	div {
		display: flex;
		flex-wrap: wrap;
		gap: var(--layout-gap);
		width: var(--size-full);
	}

	.hide {
		display: none;
	}
	.compact > :global(*),
	.compact :global(.box) {
		border-radius: 0;
	}
	.compact,
	.panel {
		border-radius: var(--container-radius);
		background: var(--color-background-secondary);
		padding: var(--size-2);
	}
	.unequal-height {
		align-items: flex-start;
	}

	.stretch {
		align-items: stretch;
	}

	div > :global(*),
	div > :global(.form > *) {
		flex: 1 1 0%;
		flex-wrap: wrap;
		min-width: min(160px, 100%);
	}
</style>
