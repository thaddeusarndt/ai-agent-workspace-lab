from __future__ import annotations

import argparse
import json
from pathlib import Path

from .report_builder import render_trace_report
from .task_runner import run_workspace


def main() -> None:
    parser = argparse.ArgumentParser(description="Run a simulated agent workspace dry-run trace.")
    parser.add_argument("--config", default="examples/mock_workspace_config.json")
    parser.add_argument("--output", default="reports/generated/dry_run_trace.md")
    args = parser.parse_args()
    config = json.loads(Path(args.config).read_text())
    trace = run_workspace(config)
    report = render_trace_report(trace)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(report)
    print(out)


if __name__ == "__main__":
    main()
