from agent_workspace_lab.report_builder import render_trace_report


def test_render_trace_report_includes_clean_room_banner_and_decisions():
    trace = [
        {"task_id": "1", "tool": "summarizer", "decision": "allow", "reason": "local low-risk tool", "mode": "dry_run"},
        {"task_id": "2", "tool": "message_sender", "decision": "needs_approval", "reason": "external action", "mode": "dry_run"},
    ]

    report = render_trace_report(trace)

    assert report.startswith("# AI Agent Workspace Dry-Run Trace")
    assert "simulated clean-room demo" in report.lower()
    assert "message_sender" in report
    assert "needs_approval" in report
