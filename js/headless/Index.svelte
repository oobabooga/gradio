<script lang="ts">
    import { Block } from "@gradio/atoms";
    import type { LoadingStatus } from "@gradio/statustracker";

    export let value: string = "";
    export let callback: string = "handleMorphdomUpdate";
    export let loading_status: LoadingStatus | undefined = undefined;
    export let elem_id: string = "";
    export let elem_classes: string[] = [];
    export let visible: boolean = true;
    export let gradio: any;

    // Call the global callback function whenever value changes
    $: {
        if (typeof window !== 'undefined' && value !== undefined) {
            const callbackFn = (window as any)[callback];
            if (typeof callbackFn === 'function') {
                callbackFn(value);
            } else {
                console.warn(`Headless component: callback function '${callback}' not found on window`);
            }
        }
    }
</script>

<!-- Render nothing -->
<div class="headless-component" style="display: none;" id={elem_id}>
    <!-- No visual content -->
</div>
