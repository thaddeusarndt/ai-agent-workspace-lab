from __future__ import annotations

from typing import Any


class ToolRegistry:
    def __init__(self, tools: dict[str, dict[str, Any]]):
        self._tools = tools

    @classmethod
    def from_config(cls, config: dict[str, Any]) -> "ToolRegistry":
        return cls({tool["name"]: dict(tool) for tool in config.get("tools", [])})

    def get(self, name: str) -> dict[str, Any]:
        if name in self._tools:
            return dict(self._tools[name])
        return {"name": name, "surface": "unknown", "risk": "blocked"}
