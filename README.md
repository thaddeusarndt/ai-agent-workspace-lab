# AI Agent Workspace Lab

Simulated clean-room agent workspace patterns for task routing, mock tools, approval boundaries, and dry-run orchestration.

This repo is public proof-of-work for AI workflow design, not a dump of private assistant infrastructure. It uses synthetic tasks, mock tools, and deterministic policy checks to show how agent-like workflows can be made auditable and human-reviewable.

## Safety boundary

This is a clean-room reference demo. It does **not** include real hostnames, IP addresses, private paths, raw chats, assistant memory, gateway layouts, credentials, platform sessions, personal account data, scheduled production jobs, or live external actions.

## What it demonstrates

- Mock tool registry
- Policy decisions for allow / approval-required / blocked actions
- Dry-run task routing
- Markdown trace reports
- Tests and GitHub Actions CI

## Example

```bash
PYTHONPATH=src python -m agent_workspace_lab.demo   --config examples/mock_workspace_config.json   --output reports/generated/dry_run_trace.md
```

Run tests:

```bash
PYTHONPATH=src pytest -q
```

## Framing

The goal is to show clean workflow architecture: separate routing from policy, require approval for external actions, block dangerous actions, and generate a trace that a human can review.
