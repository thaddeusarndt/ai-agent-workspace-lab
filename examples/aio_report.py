"""Offline aggregate report: referrals and confirmed bookings remain distinct."""
import json
from pathlib import Path
import sys


def render(data):
    for key in ("confirmed_chatgpt_discovery_bookings", "chatgpt_sessions", "chatgpt_engaged_sessions"):
        value = data.get(key)
        if type(value) is not int or value < 0:
            raise ValueError(f"{key} must be a nonnegative integer")
    if data["chatgpt_engaged_sessions"] > data["chatgpt_sessions"]:
        raise ValueError("Engaged sessions cannot exceed total sessions")
    return "\n".join([
        "# AI discovery outcome report",
        f"As of {data['as_of']}; analytics window: {data['analytics_window']}.",
        f"Confirmed ChatGPT-discovery bookings: {data['confirmed_chatgpt_discovery_bookings']}",
        f"ChatGPT referral sessions: {data['chatgpt_sessions']}",
        f"Engaged ChatGPT sessions: {data['chatgpt_engaged_sessions']}",
        "Conversion rate: not computed; these counts are not a joined cohort.",
        "Revenue: unknown. Causal lift from individual changes: unknown.",
    ])


if __name__ == "__main__":
    print(render(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))))
