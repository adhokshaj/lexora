# Lexora 5.1 QA and review results

## Gates

- Product scope: pass
- Design QA: pass
- Engineering review: pass
- Security/privacy review: pass, conditional on green browser CI
- Static JavaScript syntax: pass
- Worker unit/security tests: pass
- Secret-pattern and service-worker checks: pass
- Patch whitespace: pass
- Chromium E2E: pending GitHub Actions
- WebKit E2E: pending GitHub Actions
- User acceptance: pending staging review

## Automated feature coverage

- Inline word keyboard navigation and exclusion inside an existing button
- Common function-word suppression
- Note draft retention across navigation, explicit save, and whitespace preservation
- Valid curated collection preview
- Unknown local words excluded from persistence
- Unsafe source schemes excluded from rendering
- Normalized collection request cache reused while offline
- Worker rejection for short prompts and unsafe model output
- Existing search, bookmark, history, offline dictionary, lesson resume, AI cache, daily budget, and mobile/error scenarios remain in the suite

## Environment note

Playwright is not installed and network installation is blocked in the isolated local workspace. The authoritative Chromium and WebKit executions therefore remain required pull-request checks on their existing supported runners. No production deployment is authorized by this document.

## Nonblocking hardening backlog

- Broader prompt-injection and malicious-output corpus
- Forced local-storage failure browser test
- Full link-exclusion selector matrix
- Per-user rate-limit partitioning if the worker becomes multi-user
