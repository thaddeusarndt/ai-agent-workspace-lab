# Scheduled systems I build and operate

These are selected patterns from my Hermes, Codex, and Claude Code work. Production runs are private. The examples here rebuild the useful engineering patterns with synthetic inputs.

| System | Repeated job | What a person receives |
|---|---|---|
| AI discovery reporting | Read existing assistant-referral analytics and keep attribution types separate | Referral counts and separately confirmed business outcomes |
| Service-page gap radar | Compare service questions with published answers | Source-backed writing and page improvements for review |
| Site quality checks | Inspect mobile layouts, links, metadata, and deployment parity | Evidence of what failed and a bounded repair proposal |
| Lesson lead operations | Reconcile several lead sources and detect incomplete coverage | A reviewable queue that exposes missing inputs |
| Bookmark intake | Deduplicate new saved sources before synthesis | A small set of useful actions; no model wake when nothing is new |
| Content planning | Turn an approved claim and writing guide into native platform drafts | Exact post copy with an explicit account and approval boundary |
| Fleet history | Inventory sessions across machines and separate capture from completed write-ups | A project handoff with unresolved work still visible |
| Automation health | Check failed runs, stale evidence, and ownership of running services | A failure receipt or a verified recovery, rather than hidden retries |

## Engineering choices

I care about the second run as much as the first. Replayed inputs should not create duplicate actions. A failed collector should not report “nothing found.” An expired account token should stop publication. A successful upload should not be called a production deployment until the public site serves it.

The public `examples/cron_replay.py` demonstration exercises successful collection, duplicate delivery suppression, incomplete coverage, and retry after failure. It sends nothing and runs no scheduler.

## Current limits

Autolabel is early-stage. The content systems prepare drafts; public publishing depends on the target account being connected and the exact copy being approved. The lesson discovery result is a business outcome, not evidence that every automation is unattended or that a particular SEO change caused the bookings.

The private operations system includes additional customer and research work. This catalog intentionally documents behavior without publishing private prompts, customer records, machine addresses, or unreleased product plans.
