# Lexora 5.1 security and privacy review

- Exact configured origin and bearer-token checks remain before AI or retrieval work.
- Existing rate limiting and request-size limits remain active.
- Collection prompts are bounded to 300 characters and treated as untrusted reference text.
- Model output is parsed and allow-listed on the worker and validated again in the browser.
- Titles, descriptions, and words reject controls, markup, URLs, invalid lengths, and duplicates.
- Source links come from server retrieval and must be HTTPS.
- UI output is escaped before insertion; linked words are built with DOM APIs.
- AI previews do not mutate durable state. Only explicit save writes known dictionary words.
- Notes announce success only after local persistence succeeds; failed saves restore the stored value.
- Privacy copy warns users not to enter confidential information.
