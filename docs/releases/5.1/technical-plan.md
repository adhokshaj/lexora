# Lexora 5.1 technical and release plan

## Company-style pipeline

1. Product: scope, compatibility, and acceptance criteria.
2. Design: interaction, copy, responsive behavior, and accessibility.
3. Architecture: client/worker contract and storage boundaries.
4. Security/privacy: authentication, origin, prompt, output, and source validation.
5. Engineering: implementation on `feature/lexora-5.1`.
6. QA: unit, syntax, Chromium, WebKit, offline, and regression evidence.
7. Design QA: desktop/mobile/light/dark/reduced-motion review.
8. User acceptance: staging approval.
9. Release: reviewed pull request into `main`.
10. Production verification: Pages build, cache version, smoke test, rollback readiness.

## Compatibility

Keep `lexora-v1`, `lexora-v4-content`, tutor settings, and backup schemas unchanged. Custom collections remain arrays of local dictionary keys. The service-worker cache is versioned only when the release candidate is complete.

## API contract

`kind: "curate"` accepts a normalized prompt (maximum 300 characters), approximate level, interests, recent words, and existing titles. The worker returns `{collection:{title,description,words},sources,generatedAt}`. Client and worker validate lengths, uniqueness, control characters, and HTTPS-only server-generated sources.
