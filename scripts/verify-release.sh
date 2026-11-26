#!/usr/bin/env bash
set -euo pipefail
root_dir="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root_dir"
node worker/test.mjs
for file in app.js online.js quality.js sw.js; do node --check "$file"; done
if grep -RniE '(api[_-]?key|private[_-]?key|bearer)[[:space:]]*[:=][[:space:]]*["'\''`][A-Za-z0-9_./+-]{16,}' worker .github app.js online.js quality.js; then
  echo 'Potential committed secret found.' >&2
  exit 1
fi
cache_name="$(sed -n "s/^const CACHE='\([^']*\)'.*/\1/p" sw.js)"
test -n "$cache_name"
grep -q "'./quality.js'" sw.js
grep -q "'./quality.css'" sw.js
if find . -type d -name __pycache__ -o -type f \( -name '*.pyc' -o -name '*.pyo' \) | grep -q .; then
  echo 'Generated Python artifacts found; remove them before release.' >&2
  exit 1
fi
if [[ "${LEXORA_E2E:-0}" == "1" ]]; then
  python qa/e2e.py . --browser chromium
  python qa/e2e.py . --browser webkit
else
  echo 'PASS static and worker checks (set LEXORA_E2E=1 for both browsers)'
fi
