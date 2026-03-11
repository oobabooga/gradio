"""gr.DragDrop() component."""

from __future__ import annotations

from typing import Any, Callable

from gradio.components.base import FormComponent
from gradio.events import Events


class DragDrop(FormComponent):
    """
    Creates a drag-and-drop reorderable list of items. Items are displayed as
    draggable boxes that can be rearranged. The value is a newline-separated
    string of item names, compatible with gr.Textbox for drop-in replacement.
    """

    EVENTS = [
        Events.change,
        Events.input,
    ]

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        label: str | None = None,
        info: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | None = None,
    ):
        """
        Parameters:
            value: Default value as a newline-separated or comma-separated string of item names.
            label: The label for this component.
            info: Additional component description.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open.
            show_label: If True, will display label.
            container: If True, will place the component in a container.
            scale: Relative size compared to adjacent Components.
            min_width: Minimum pixel width.
            interactive: If True, items can be reordered by dragging.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM.
            render: If False, component will not be rendered in the Blocks context.
            key: If assigned, will be used to assume identity across a re-render.
        """
        super().__init__(
            label=label,
            info=info,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            key=key,
            value=value,
        )

    def preprocess(self, payload: str | None) -> str | None:
        """
        Parameters:
            payload: the newline-separated string of item names.
        Returns:
            Passes the value as a {str} into the function.
        """
        return None if payload is None else str(payload)

    def postprocess(self, value: str | None) -> str | None:
        """
        Parameters:
            value: Expects a {str} of newline or comma separated item names.
        Returns:
            The value to display as draggable items.
        """
        return None if value is None else str(value)

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}

    def example_payload(self) -> Any:
        return "item_a\nitem_b\nitem_c"

    def example_value(self) -> Any:
        return "item_a\nitem_b\nitem_c"
