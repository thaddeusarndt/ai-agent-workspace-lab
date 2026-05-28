# AI Agent Workspace Dry-Run Trace

> This is a simulated clean-room demo. It uses mock tools and synthetic tasks only; it does not include real infrastructure, hostnames, IPs, private logs, assistant memory, credentials, or live actions.

## Decisions

- Task `task-001` via `summarizer`: `allow` (dry_run)
  - Reason: local low-risk tool allowed in dry-run mode
- Task `task-002` via `draft_writer`: `allow` (dry_run)
  - Reason: local low-risk tool allowed in dry-run mode
- Task `task-003` via `message_sender`: `needs_approval` (dry_run)
  - Reason: external or elevated-risk action requires human approval: external/high
- Task `task-004` via `payment_action`: `blocked` (dry_run)
  - Reason: tool is explicitly blocked in this simulated workspace
