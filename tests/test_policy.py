from agent_workspace_lab.policy import decision_for_tool


def test_policy_allows_low_risk_local_tools():
    decision = decision_for_tool({"name": "summarizer", "surface": "local", "risk": "low"})

    assert decision.status == "allow"
    assert decision.requires_approval is False


def test_policy_requires_approval_for_external_high_risk_tools():
    decision = decision_for_tool({"name": "message_sender", "surface": "external", "risk": "high"})

    assert decision.status == "needs_approval"
    assert decision.requires_approval is True
    assert "external" in decision.reason


def test_policy_blocks_explicitly_blocked_tools():
    decision = decision_for_tool({"name": "payment_action", "surface": "external", "risk": "blocked"})

    assert decision.status == "blocked"
    assert decision.requires_approval is True
