# Command Centre Connectors

Status: capability spec — pending build
Date: 2026-05-15
Owner: Wayne Francis

## Purpose

Axis Local OS becomes a command centre when it can read from and act on the operator's working tools — Outlook, Microsoft 365, Google Workspace, Gmail, Drive, Calendar, Teams, Slack, and the same shape for any other business platform. This spec defines how that happens without compromising the governance, audit, and data discipline the rest of the system depends on.

Security is the first design constraint. Capability is the second. A connector that fails the security model is not built, even if the platform is popular.

## First Principle

A connector is a governed extension of the operator's existing authority. Axis never gets capability the operator did not consent to, never holds credentials in plaintext, never sends connector data outside the operator's machine without an explicit approval, and never acts on the operator's behalf without an audit event.

If a connector cannot meet those four conditions, it does not ship.

## Security Model

### Authentication

- All connectors use **OAuth 2.0** (or vendor-equivalent token-based auth). Never username and password.
- Axis requests the **minimum scopes** required for the use case, never blanket access. Read-only scopes by default; write scopes are added per use case under explicit consent.
- Each OAuth grant is **per-account, per-purpose**. Wayne's personal Outlook and a client's Outlook are separate grants with separate tokens.

### Credential Storage

- Access and refresh tokens are stored in the **operating system's native secret store**: Windows Credential Manager on Windows, Keychain on macOS, Secret Service on Linux.
- Tokens are **never written to disk in plaintext**, never in JSON files, never in audit logs, never in environment variables that another process can read.
- A token vault index lives at `business/CONNECTORS/<connector>/<account>/INDEX.md` with metadata only — display name, scopes granted, last refreshed, expiry, status. No secret material.
- The vault provides one operation: `get_token(connector, account)` — returns a short-lived bearer string. The caller may not cache it.

### Network Discipline

- Connectors call vendor APIs over **HTTPS with certificate verification on** — no `verify=False`, ever.
- Vendor endpoints are pinned to the documented production hostnames. Endpoint overrides require a typed confirm phrase, same as destructive coding-agent actions.
- No connector calls a third-party intermediary. Direct from Axis to vendor only.

### Data Flow

- Data fetched from a connector enters the local Axis store **only when the operator chooses to ingest it**. By default, connector reads are query-time and not retained.
- When ingested, fetched data carries the same metadata discipline as any other source: `source_id`, modified_at, scope flag (internal_only or outbound_ok), and the connector account it came from.
- Connector data flagged `internal_only` is **never sent to a hosted model** — the existing source-scope filter from the hosted adapter spec applies.
- The operator can choose to mark an entire connector account as `local_only`, blocking all hosted-model use of data from that account.

### Audit

Every connector call writes an event to `.axis/audit/connectors.jsonl` with:

- `connector` — outlook / gmail / drive / etc.
- `account_id` — opaque identifier (no email body, no display name unless explicitly opted in)
- `operation` — read_messages / send_email / create_event / etc.
- `scope_used` — the OAuth scope actually exercised
- `request_summary` — operation parameters, never message bodies in full
- `approval_level` — none / review / approval / approval+confirm
- `approval_proof` — preview_hash or confirm_phrase_matched flag for approval-level operations
- `outcome` — success / failure / blocked
- `bytes_in` / `bytes_out` — for cost and load tracking
- `latency_ms` — vendor response time

Tokens never appear in the audit. Message bodies are referenced by ID and stored in the connector's own system, not duplicated to the audit.

## Approval Model

Connector operations inherit the same approval-level vocabulary as the coding agent.

| Level | Examples | Default |
|---|---|---|
| `none` | List recent emails, list calendar events for today, count unread, check service status | allowed |
| `review` | Read a specific email body, read an attachment, ingest a folder into the local KB | requires review before content is exposed to the model |
| `approval` | Send an email, create or move a calendar event, save a file, post a Slack message, share a Drive link | requires preview_hash approval |
| `approval+confirm` | Delete an email, delete a calendar event, revoke a sharing link, move to trash, mass-mailing operations, anything that affects more than one record | requires preview_hash plus typed confirm phrase |

The level applies to the **operation**, not the connector. Same connector can run all four levels depending on what is asked.

## Per-Client Scoping

When Wayne runs Axis on behalf of a client, the client's connector grants are isolated in `business/CLIENTS/<slug>/CONNECTORS/`. The DCoS routing layer enforces:

- A request scoped to client A cannot use connector tokens from client B.
- A request scoped to Wayne's own ops cannot use client connector tokens.
- Cross-client operations are explicitly blocked unless the user is in an explicit multi-client review mode and approves each call.
- The audit event records the active client scope at the time of the call.

## Initial Connector Catalogue

The first build wave covers the most common business platforms. Each ships with a documented scope list, an approval-level map per operation, and an integration test plan.

### Wave 1 — Email and Calendar

- **Microsoft 365 / Outlook** (mail, calendar, contacts) via Microsoft Graph API
- **Google Workspace / Gmail** (mail, calendar, contacts) via Google Workspace API
- **iCloud Mail / Calendar** — read-only via IMAP/CalDAV (deferred, requires app-specific password)

### Wave 2 — Files and Storage

- **OneDrive / SharePoint** via Microsoft Graph API
- **Google Drive / Docs / Sheets** via Google Drive API
- **Dropbox** via Dropbox API
- **Box** via Box API

### Wave 3 — Messaging and Meetings

- **Microsoft Teams** (channels, chat, meetings) via Microsoft Graph API
- **Slack** via Slack API
- **Zoom** (meetings, recordings) via Zoom API
- **Google Meet** via Google Workspace API

### Wave 4 — CRM and Pipeline

- **HubSpot** (contacts, deals, notes) via HubSpot API
- **Salesforce** via Salesforce REST API
- **Pipedrive** via Pipedrive API
- **Apollo** (existing MCP integration retained where useful)

### Wave 5 — Finance and Operations

- **Xero** (accounts, invoices) — read-only by default
- **QuickBooks** — read-only by default
- **Stripe** — read-only by default (never charge on user behalf without approval+confirm)

The catalogue is not a roadmap commitment for all waves. It is the documented surface area so Wayne can prioritise which connectors get built first based on real customer demand.

## Connector Interface Contract

Every connector implements a small set of functions so the rest of Axis treats them uniformly.

```text
authenticate(account_alias)          -> stores tokens in OS keychain
revoke(account_alias)                -> revokes vendor side and clears local index
health(account_alias)                -> reachable, scopes valid, expiry
list(operation, parameters)          -> level `none` reads
read(operation, item_id)             -> level `review` reads
preview_write(operation, payload)    -> level `approval`/`+confirm` preview, returns preview_hash
apply_write(operation, payload, h)   -> executes a previewed write
ingest(operation, parameters)        -> imports into local KB with metadata
```

The preview / apply / hash pattern is the same one the coding agent already uses. Connector writes are never one-shot. They always go through preview first.

## OAuth Flow Hardening

- PKCE is mandatory for any connector that supports it.
- Refresh tokens are short-lived where the vendor allows (Microsoft Graph) and rotated on use.
- Token-grant flows run in a local loopback redirect (`http://localhost:<random-port>`), never an open redirect.
- Consent screens display the exact scope list to the operator before grant.
- Grant logs are append-only at `business/CONNECTORS/<connector>/<account>/GRANT_LOG.md` — every consent, refresh, revoke recorded with timestamp and scope.
- A revoke command is always available and removes both the vendor-side grant and the local vault entry in one operation.

## Disconnect And Revocation

Every connector exposes a one-step revoke that:

1. Calls the vendor's revoke endpoint to invalidate the access token on the vendor side.
2. Removes refresh tokens from the OS keychain.
3. Clears the local INDEX.md entry.
4. Optionally deletes any ingested KB chunks tagged with that connector account.
5. Writes a final audit event recording the revoke.

If any step fails (vendor revoke endpoint down), the others still complete and the audit records partial-revoke status so Wayne can retry later.

## Forbidden Patterns

The following are not implemented at any tier:

- Storing OAuth client secrets in code or config files. Client IDs are public; secrets live in the vault.
- Polling a vendor API more frequently than its documented rate limit.
- Caching message bodies or file contents in audit logs.
- Sending connector data to a hosted model without the source-scope filter.
- Acting on multiple recipients in a single approval (mass mailing). Mass operations split into per-recipient approvals.
- Acting on data from a client scope while operating in another client's scope.
- Auto-renewing a grant whose scope has expanded since the original consent.

## MVP Build Order

1. Spec + module registration (this file + entry in `axis_modules.py`).
2. OS keychain wrapper at `tools/local_os/secrets.py` (Windows Credential Manager + cross-platform stubs).
3. OAuth loopback grant flow at `tools/local_os/oauth.py` (PKCE, local port, scope display).
4. Connector interface contract (Python abstract base class).
5. Microsoft Graph connector — read mail / read calendar / send mail / create event. Approval levels per operation.
6. Google Workspace connector — same shape.
7. Per-client scope enforcement in DCoS routing.
8. Connector audit log + revoke command.
9. Wave 2 storage connectors (OneDrive, Drive, Dropbox, Box).
10. Wave 3 messaging connectors (Teams, Slack).
11. Wave 4 CRM connectors.
12. Wave 5 finance connectors (read-only).

## First CLI Surface

```powershell
python tools/local_os/axis_connectors.py list
python tools/local_os/axis_connectors.py authenticate outlook --account wayne
python tools/local_os/axis_connectors.py health outlook --account wayne
python tools/local_os/axis_connectors.py read-mail outlook --account wayne --since 2026-05-14
python tools/local_os/axis_connectors.py preview-send outlook --account wayne --to a@b.com --subject "..." --body-file draft.txt
python tools/local_os/axis_connectors.py apply-send outlook --account wayne --confirm <preview_hash>
python tools/local_os/axis_connectors.py revoke outlook --account wayne
```

## Governance Rules

- All connector authentication is OAuth 2.0 with PKCE where available. Never username and password.
- Tokens live in the OS keychain. Never in files, never in env, never in logs.
- Minimum-scope grants. No blanket access. New scopes require fresh consent.
- Every connector call writes an audit event. Token material is never in the audit.
- Writes go through preview + approval_hash, same pattern as the coding agent.
- Destructive and mass operations require typed confirm phrase.
- Per-client scopes isolate connector grants. No cross-client access without explicit multi-client mode.
- Connector data is local by default. Hosted-model use of connector data requires the source-scope filter to pass.
- Revoke is always available, one step, and always audited.
- Vendor secret keys live in the vault, never in code or config.
- HTTPS with cert verification on, always. No verify=False, ever.

## What This Lets Axis Promise

> *Axis can act as your command centre across Outlook, Microsoft 365, Google, and the other tools your business already runs on. It connects with OAuth, asks for the smallest possible permissions, keeps your tokens in the operating system's own secure store, and shows you every action before it happens. It writes a receipt for everything it does. If you ever want it disconnected, one command revokes the grant and clears the local copy. Your client data does not leave your machine unless you say so, in writing, per request.*

## Success Condition

Wayne can authenticate to his Outlook, Gmail, OneDrive, and Drive, see a unified weekly view across all of them inside Axis, draft and send a reply with one approval per send, and trust that no token, no message body, and no client data ever leaves the governance layer he can see.
