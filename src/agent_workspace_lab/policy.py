from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Decision:
    status: str
    requires_approval: bool
    reason: str


def decision_for_tool(tool: dict[str, Any]) -> Decision:
    risk = str(tool.get("risk", "blocked")).lower()
    surface = str(tool.get("surface", "unknown")).lower()
    if risk == "blocked":
        return Decision("blocked", True, "tool is explicitly blocked in this simulated workspace")
    if surface == "external" or risk in {"high", "medium"}:
        return Decision("needs_approval", True, f"external or elevated-risk action requires human approval: {surface}/{risk}")
    return Decision("allow", False, "local low-risk tool allowed in dry-run mode")
