"""Synthetic cron-run contract. No scheduling, network, or external writes."""
from dataclasses import dataclass, field


@dataclass
class RunLedger:
    completed: set = field(default_factory=set)

    def run(self, run_key, source_complete, findings):
        if not source_complete:
            return {"status": "coverage_incomplete", "delivery": None, "retryable": True}
        if run_key in self.completed:
            return {"status": "duplicate_suppressed", "delivery": None, "retryable": False}
        self.completed.add(run_key)
        if not findings:
            return {"status": "complete_no_hit", "delivery": None, "retryable": False}
        return {"status": "candidate", "delivery": {"kind": "draft_report", "items": findings}, "retryable": False}


if __name__ == "__main__":
    ledger = RunLedger()
    for key, complete, findings in [("run-a", True, ["Review one broken link"]), ("run-a", True, ["Review one broken link"]), ("run-b", False, []), ("run-b", True, [])]:
        print(ledger.run(key, complete, findings))
