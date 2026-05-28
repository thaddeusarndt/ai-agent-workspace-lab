# Architecture

The demo has four small components:

1. `ToolRegistry` loads mock tools from a synthetic config.
2. `policy.decision_for_tool` classifies each tool as allowed, approval-required, or blocked.
3. `task_runner.run_workspace` routes synthetic tasks through the registry and policy.
4. `report_builder.render_trace_report` creates a markdown dry-run trace for human review.

Everything runs locally with synthetic data and no network calls.
