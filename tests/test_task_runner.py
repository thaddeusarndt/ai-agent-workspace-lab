from agent_workspace_lab.task_runner import run_workspace


def test_run_workspace_routes_tasks_to_allow_approval_and_blocked_buckets():
    config = {
        "tools": [
            {"name": "summarizer", "surface": "local", "risk": "low"},
            {"name": "message_sender", "surface": "external", "risk": "high"},
            {"name": "payment_action", "surface": "external", "risk": "blocked"},
        ],
        "tasks": [
            {"id": "1", "intent": "summarize", "requested_tool": "summarizer", "payload": {}},
            {"id": "2", "intent": "send", "requested_tool": "message_sender", "payload": {}},
            {"id": "3", "intent": "pay", "requested_tool": "payment_action", "payload": {}},
        ],
    }

    trace = run_workspace(config)

    statuses = {item["task_id"]: item["decision"] for item in trace}
    assert statuses == {"1": "allow", "2": "needs_approval", "3": "blocked"}
    assert all(item["mode"] == "dry_run" for item in trace)
