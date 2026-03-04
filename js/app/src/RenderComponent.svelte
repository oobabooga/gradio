<svelte:options immutable={true} />

<script lang="ts">
	import type { Gradio } from "./gradio_helper";
	import type { ComponentMeta, ThemeMode } from "./types";
	import type { SvelteComponent, ComponentType } from "svelte";
	// @ts-ignore
	import { bind, binding_callbacks } from "svelte/internal";

	export let root: string;
	export let component: ComponentMeta["component"];
	export let target: HTMLElement;
	export let theme_mode: ThemeMode;
	export let instance: ComponentMeta["instance"];
	export let value: any;
	export let gradio: Gradio;
	export let elem_id: string;
	export let elem_classes: string[];
	export let _id: number;

	const s = (id: number, p: string, v: any): CustomEvent =>
		new CustomEvent("prop_change", { detail: { id, prop: p, value: v } });

	function wrap(
		component: ComponentType<SvelteComponent>
	): ComponentType<SvelteComponent> {
		const ProxiedMyClass = new Proxy(component, {
			construct(_target, args: Record<string, any>[]) {
				//@ts-ignore
				const instance = new _target(...args);
				const props = Object.keys(instance.$$.props);

				function report(props: string) {
					return function (propargs: any) {
						const ev = s(_id, props, propargs);
						target.dispatchEvent(ev);
					};
				}
				props.forEach((v) => {
					binding_callbacks.push(() => bind(instance, v, report(v)));
				});

				return instance;
			}
		});

		return ProxiedMyClass;
	}

	const _component = wrap(component);

	let cached_rest: Record<string, any> = {};
	$: {
		const rest = $$restProps;
		let changed = Object.keys(rest).length !== Object.keys(cached_rest).length;
		if (!changed) {
			for (const k in rest) {
				if (rest[k] !== cached_rest[k]) {
					changed = true;
					break;
				}
			}
		}
		if (changed) {
			cached_rest = rest;
		}
	}
</script>

<svelte:component
	this={_component}
	bind:this={instance}
	bind:value
	on:prop_change
	{elem_id}
	{elem_classes}
	{target}
	{...cached_rest}
	{theme_mode}
	{root}
	{gradio}
>
	<slot />
</svelte:component>
