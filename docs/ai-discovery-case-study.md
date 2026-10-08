# Six lesson students found me through ChatGPT

I teach piano, Ableton, music production, and songwriting in Los Angeles and online. As of October 7, 2026, six students who booked lessons had each told me they found my lessons through ChatGPT before reaching out.

I built and operate the site's discovery and measurement system with Hermes, Codex, and Claude Code. It checks the public service pages, finds unanswered service questions, prepares writing for review, and measures assistant referrals on the existing reporting cadence.

## What the result establishes

| Measure | Observed result | Evidence boundary |
|---|---:|---|
| Students confirming ChatGPT discovery and booking | 6 | Confirmed by the business owner from student conversations; cumulative, with no published customer identities |
| ChatGPT referral sessions, August 12–October 6, 2026 | 40 | Aggregate GA4 source measurement; not matched to individual students |
| Engaged ChatGPT sessions in that window | 23 | An analytics engagement measure, not a booking count |

The student reports and referral sessions are separate measurements. They cannot be added or divided to calculate a conversion rate. Revenue, retention, and the causal contribution of individual page changes have not been established here.

## How the engine works

1. Check that the current site and the version under review agree.
2. Inspect service pages and the questions a prospective student needs answered.
3. Prepare source-backed changes using an approved writing guide.
4. Review the exact proposed public copy before releasing it.
5. Verify the released pages and record the deployment.
6. Report referral sessions separately from confirmed discovery, bookings, and payments.

Examples of questions the site addresses: which instrument or software is taught, whether lessons are online or in Los Angeles, what the first lesson costs, and what happens after booking.

The public teaching site is [thaddeusarndt.com](https://thaddeusarndt.com/). [Preballin](https://preballin.com/) is my automation studio; [Autolabel](https://autolabel.studio/) is the early-stage artist operations product I am building through it.

## Reproduce the measurement boundary

Run `python examples/aio_report.py examples/aio_aggregate.json` from this repository. This public reference example uses the published aggregate counts above. It makes no network calls and contains no student records, credentials, production prompts, or private source lists.

The reference implementation demonstrates the reporting contract. It is a small public reconstruction, not an export of the production acquisition system.
