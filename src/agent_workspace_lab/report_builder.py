from __future__ import annotations


def render_trace_report(trace: list[dict[str, str]]) -> str:
    lines = [
        "# AI Agent Workspace Dry-Run Trace",
        "",
        "> This is a simulated clean-room demo. It uses mock tools and synthetic tasks only; it does not include real infrastructure, hostnames, IPs, private logs, assistant memory, credentials, or live actions.",
        "",
        "## Decisions",
        "",
    ]
    for item in trace:
        lines.append(f"- Task `{item['task_id']}` via `{item['tool']}`: `{item['decision']}` ({item['mode']})")
        lines.append(f"  - Reason: {item['reason']}")
    lines.append("")
    return "\n".join(lines)
