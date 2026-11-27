## Product and design

- [ ] Product brief and acceptance criteria reviewed
- [ ] Design QA completed in light/dark and desktop/mobile modes
- [ ] Keyboard, touch, focus, and reduced-motion behavior reviewed

## Engineering and safety

- [ ] Existing storage and backup formats remain compatible
- [ ] Worker input/output validation and privacy copy reviewed
- [ ] No secrets or production credentials committed
- [ ] Service-worker cache version is consistent

## Verification

- [ ] `scripts/verify-release.sh` passes
- [ ] Chromium E2E passes
- [ ] WebKit E2E passes
- [ ] Staging UAT approved
- [ ] Rollback point recorded before production deployment
