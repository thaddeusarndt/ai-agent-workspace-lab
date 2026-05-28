from agent_workspace_lab.tool_registry import ToolRegistry


def test_registry_returns_declared_mock_tool():
    registry = ToolRegistry.from_config({"tools": [{"name": "summarizer", "surface": "local", "risk": "low"}]})

    assert registry.get("summarizer")["name"] == "summarizer"


def test_registry_marks_unknown_tool_as_blocked():
    registry = ToolRegistry.from_config({"tools": []})

    tool = registry.get("unknown_tool")

    assert tool["name"] == "unknown_tool"
    assert tool["risk"] == "blocked"
