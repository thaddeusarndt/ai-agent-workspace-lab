from __future__ import annotations

from typing import Any

from .policy import decision_for_tool
from .tool_registry import ToolRegistry


def run_workspace(config: dict[str, Any]) -> list[dict[str, str]]:
    registry = ToolRegistry.from_config(config)
    trace = []
    for task in config.get("tasks", []):
        tool = registry.get(task.get("requested_tool", "unknown_tool"))
        decision = decision_for_tool(tool)
        trace.append({
            "task_id": str(task.get("id", "unknown")),
            "intent": str(task.get("intent", "unknown")),
            "tool": str(tool.get("name", "unknown_tool")),
            "decision": decision.status,
            "requires_approval": str(decision.requires_approval).lower(),
            "reason": decision.reason,
            "mode": "dry_run",
        })
    return trace
