LEXORA — Make words yours. / Starter version

Install on iPhone (no Xcode):
1. Unzip Lexora.zip on a computer. The folder contains index.html, app.js, data.js, manifest.json, sw.js and icons.
2. Publish the folder as a static HTTPS website using a host such as GitHub Pages. A free public GitHub repository works: create a repository, upload the files in the folder (not the ZIP), open Settings > Pages, choose Deploy from a branch, main, /(root), Save. Open the published URL once it is available.
3. Open that HTTPS URL in Safari on iPhone, use Share > Add to Home Screen (if offered, keep Open as Web App enabled), then Add.
4. Open the installed icon while online first so the service worker can cache files. Try airplane mode and reopen to confirm offline operation. Pronunciation depends on available device voices. Updates require online access and may need the web app to be closed and reopened.

Optional computer preview: run python3 -m http.server 8000 inside the folder and open http://localhost:8000. This is not an iPhone installation URL.

149 original starter entries, 22 curated topic collections plus dynamic playlists. Only selected entries include examples/synonyms/antonyms. Import additional dictionary JSON from Profile, mapping words to definitions or objects with d, level (1–4), e, s, a. Storage is local, browser quota applies; export backups regularly. No external API, analytics or mandatory account. No automatic capture of Apple Spotlight searches, no native share extension, no live slang feed, no native notifications. Assessment is heuristic, not an official CEFR score. Review scheduling uses a basic adaptive interval rule, not Vocabulary.com's proprietary algorithm. JavaScript syntax and basic logic smoke-tested; no physical iPhone or browser end-to-end test performed. Full dictionary download was unavailable in the build environment.
