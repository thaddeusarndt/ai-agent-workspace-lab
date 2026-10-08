# Scheduled systems I build and operate

These are selected systems from my Hermes, Codex, and Claude Code work. Production runs are private. This repository includes selected operating functions and reference demonstrations with aggregate or synthetic inputs.

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

## Selected operating code

`engines/aio_page_inspection.py` contains HTML inspection functions from the operating AIO authority radar. They inspect titles, headings, canonical tags, indexing directives and structured-data block presence. The public reader exposes file errors instead of turning failed reads into empty pages. Private business policy, strategy documents, machine paths and delivery configuration are excluded.

`engines/cron_delivery_gates.py` contains three pure gates from the operating scheduled-job system: content-gap, health and contact-output review. Errors and unknown output wake a reviewer; successful output with no changes can stay quiet. They contain no posting or notification credentials and send nothing.

Run the local audit against the fictional static-site fixture:

```sh
python examples/aio_audit.py examples/site_snapshot --domain example.com > /tmp/aio-first.json
python examples/aio_audit.py examples/site_snapshot --domain example.com --previous /tmp/aio-first.json
python -m pytest -q
```

The second identical audit sets `wake_for_review` to false. A read failure stays visible, and restored coverage wakes review. The report describes local HTML facts; it does not measure search rankings, validate schema semantics, prove crawler access or establish attribution. It is a public subset of the acquisition system, not the entire production deployment.

## Current limits

Autolabel is early-stage. The content systems prepare drafts; public publishing depends on the target account being connected and the exact copy being approved. The lesson discovery result is a business outcome, not evidence that every automation is unattended or that a particular SEO change caused the bookings.

The private operations system includes additional customer and research work. This catalog intentionally documents behavior without publishing private prompts, customer records, machine addresses, or unreleased product plans.
