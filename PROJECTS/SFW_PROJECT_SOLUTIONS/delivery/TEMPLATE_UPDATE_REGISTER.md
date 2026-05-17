# Template Update Register

Status: production control
Purpose: Decide which master template improvements should be applied to shipped builds.

## Master Source Rule

All new builds must start from:

```text
D:\Wayne AI OS\Axis OS_v4\PROJECTS\SFW_PROJECT_SOLUTIONS\delivery\LATEST_SELLABLE_BUILDS
```

Do not create new production builds from shipped folders, test folders, archives, or duplicate copies.

## Update Register

| Date | Update | Affected Templates | Reason | Should Shipped Builds Receive This? | Priority | Client Impact | Applied To | Notes |
|---|---|---|---|---|---|---|---|---|
|  |  |  |  | yes / no / selective | high / medium / low |  |  |  |

## Decision Rule

Do not blind-copy template updates into shipped builds.

Shipped builds contain client-specific context, memory, trackers, decisions, and operating history.

Apply updates selectively:

- copy new governance files if missing
- patch instruction files
- update checklists
- add new workflow modules only if relevant
- preserve client memory, trackers, decisions, and context

## Required Shipped Build Log

Each shipped or client-ready build should include:

```text
CARE_PACKAGE/BUILD_UPDATE_LOG.md
```

The build update log records exactly what changed, why, whether approval was needed, and what test was completed.

## Simple Rule

Master templates get improved continuously.

Shipped builds get updated through care reviews, selectively, with a log.

