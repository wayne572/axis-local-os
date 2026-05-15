# Knowledge Source Registry

This registry controls what the AI Knowledge Base is allowed to index.

## Approved Source Areas

| Source area | Status | Notes |
|---|---|---|
| `README.md` | Approved | System overview |
| `START_HERE.md` | Approved | Current routing and priority |
| `PRODUCT_MANUAL/` | Approved | Product explanation and development guidance |
| `OS_GUIDES/` | Approved | User commands and operating guides |
| `CORE/` | Approved | Governance, specialist OS, validation, and learning material |
| `business/` | Approved with care | Active business memory, pricing, trackers, GDPR |
| `../final-docs-drafts/` | Approved with care | Business Bible, SOPs, templates, offer docs |
| `PROJECTS/SFW_PROJECT_SOLUTIONS/` | Approved with care | Commercial, delivery, client templates, shipped examples |

## Excluded By Default

| Pattern | Reason |
|---|---|
| `.git/` | System metadata |
| `.claude/` | Agent internals, not first-pass knowledge |
| `.kb/` | Generated index output |
| `*.zip` | Binary package |
| `*.pdf` | Later parser stage |
| `*.png`, `*.jpg`, `*.jpeg`, `*.webp` | Later multimodal stage |

## Source Metadata To Preserve

Each chunk should preserve:

- source path
- title or heading where possible
- chunk number
- last modified date if available
- source type
- indexed timestamp

## Business Safety Rule

Sensitive business/client folders can be indexed for Wayne's internal OS, but client deployments must use a client-specific registry and must not inherit Wayne's private business memory unless explicitly approved.

