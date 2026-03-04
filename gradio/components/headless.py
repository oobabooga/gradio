"""gr.Headless() component."""

from __future__ import annotations

from typing import Any

from gradio.components.base import Component
from gradio.events import Events


class Headless(Component):
    """
    Lightweight hidden component for passing data to JavaScript callbacks
    without rendering overhead. Unlike gr.JSON(visible=False), this component
    has no frontend rendering at all — it only receives data and fires events.
    """

    EVENTS = [Events.change]

    def __init__(
        self,
        value: Any = None,
        *,
        render: bool = True,
        elem_id: str | None = None,
        key: int | str | None = None,
    ):
        """
        Parameters:
            value: Default value of arbitrary type.
            render: If False, component will not be rendered in the Blocks context.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM.
            key: if assigned, will be used to assume identity across a re-render.
        """
        super().__init__(
            value=value,
            render=render,
            elem_id=elem_id,
            key=key,
            visible=False,
        )

    def preprocess(self, payload: Any) -> Any:
        return payload

    def postprocess(self, value: Any) -> Any:
        return value

    def example_payload(self) -> Any:
        return None

    def example_value(self) -> Any:
        return None

    def api_info(self) -> dict[str, Any]:
        return {"type": {}, "description": "any valid json"}

    @property
    def skip_api(self):
        return True
