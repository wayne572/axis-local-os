# Older Build Archive - 2026-05-17

Status: archive
Purpose: Keep older and duplicate build material without allowing it to become the active production source.

## Current Source Of Truth

Use current builds from:

```text
../LATEST_SELLABLE_BUILDS/
```

Current production templates:

- `01_SOLO_OPERATOR_OS_TEMPLATE_CLAUDE`
- `02_CLIENT_OS_BUILD_TEMPLATE_CLAUDE`
- `03_SOLO_OPERATOR_OS_TEMPLATE_CODEX`

## Archived From Delivery Root

Moved here because these were older live-test folders or duplicate root templates:

- `from_delivery_root/SOLO_OPERATOR_OS_CODEX_LIVE_TEST`
- `from_delivery_root/SOLO_OPERATOR_OS_LIVE_TEST`
- `from_delivery_root/SOLO_OPERATOR_OS_TEMPLATE`
- `from_delivery_root/CLIENT_OS_TEMPLATE`

## Archived From Outside Delivery

Moved here so delivery becomes the single place to find build material:

- `from_outside_delivery/client-templates`
- `from_outside_delivery/V3 Axis`

## Restore Rule

Do not create new production builds from this archive.

If a file is needed, copy the specific reviewed item into the current V4 template or client build and record the reason.

