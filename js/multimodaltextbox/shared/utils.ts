import { tick } from "svelte";

interface Value {
	lines: number;
	max_lines: number;
	text: string;
}

export async function resize(
	target: HTMLTextAreaElement | HTMLInputElement,
	lines: number,
	max_lines: number
): Promise<void> {
	if (lines === max_lines) return;
	await tick();

	const max = max_lines === undefined ? false : 21 * (max_lines + 1);
	const min = 21 * (lines + 1);

	target.style.height = "1px";

	const computed = getComputedStyle(target);
	const border_top = parseFloat(computed.borderTopWidth) || 0;
	const border_bottom = parseFloat(computed.borderBottomWidth) || 0;
	const border_total = border_top + border_bottom;

	let scroll_height;
	if (max && target.scrollHeight > max) {
		scroll_height = max;
	} else if (target.scrollHeight < min) {
		scroll_height = min;
	} else {
		scroll_height = target.scrollHeight;
	}

	target.style.height = `${scroll_height + border_total}px`;
}

export function text_area_resize(
	_el: HTMLTextAreaElement,
	_value: Value
): any | undefined {
	if (_value.lines === _value.max_lines) return;
	_el.style.overflowY = "auto";

	if (_value.text.trim()) {
		resize(_el, _value.lines, _value.max_lines);
	}
}
