from __future__ import annotations
from typing import Any, Callable
from gradio.components.base import Component
from gradio.events import Events

class Headless(Component):
    """
    A headless component that calls a global JavaScript function with Python outputs
    without rendering any UI.
    """
    
    EVENTS = [Events.change]
    
    def __init__(
        self,
        value: str | Callable | None = "",
        *,
        callback: str = "handleMorphdomUpdate",
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        **kwargs,
    ):
        self.callback = callback
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
            **kwargs,
        )

    def preprocess(self, payload: str | None) -> str | None:
        return payload

    def postprocess(self, value: str | None) -> str | None:
        return value

    def example_inputs(self) -> Any:
        return "example"

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}
