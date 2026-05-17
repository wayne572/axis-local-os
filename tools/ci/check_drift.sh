#!/usr/bin/env bash
# Axis Local OS - production line drift guard.
# Fails the build if SUPERSEDED PRICING appears in live (non-historical)
# markdown files, except in negation context ("old", "superseded",
# "do not use", "never use", "replaced by", "legacy", "in review").
#
# Why pricing only:
# Banned-term scans for "Black Map" or "Relationship Connector Mode"
# produced too many false positives because v4 documentation
# legitimately mentions these terms in negation context. The real
# damage from drift is always carried by a price tag, so a strict
# pricing scan catches it.
#
# Source of truth: business/PRICING_AUTHORITY.md
# Drift backlog (tracked, awaiting Wayne sign-off): business/DRIFT_BACKLOG.md
# Maintainer: @wayne572

set -euo pipefail

ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT"

# Paths excluded from the scan.
# 1. Historical or audit material - never live.
# 2. Test scenarios with frozen prices (SAMPLE_TESTS).
# 3. The pricing authority itself (lists superseded by design).
# 4. Reference files that legitimately quote old pricing in context.
# 5. DRIFT EXEMPT: pre-existing drift in client-facing files,
#    tracked in business/DRIFT_BACKLOG.md, pending Wayne sign-off
#    on replacement wording. Remove from this list as each is fixed.
EXCLUDES=(
  ':!ARCHIVE_NOTES/**'
  ':!TESTING/**'
  ':!**/_ARCHIVE_*/**'
  ':!**/SAMPLE_TESTS/**'
  ':!**/OPTIMISATION_*'
  ':!**/UPGRADE_LOG_*'
  ':!**/SESSION_HANDOFF_*'
  ':!CHANGELOG.md'
  ':!LEARNING_LOG.md'
  ':!LAUNCH_PROMPT.md'
  ':!OS_STARTUP_TEST.md'
  ':!business/PRICING_AUTHORITY.md'
  ':!business/PRICING_AND_LEGAL_REVIEW_*.md'
  ':!business/DRIFT_BACKLOG.md'
  ':!business/Sales/CHANGELOG.md'
  ':!CORE/LEARNING/**'
  ':!CORE/CLAUDE_OPERATOR/RELATIONSHIP_CONNECTOR_MODE.md'
  ':!tools/ci/**'
  ':!.github/**'
  # --- DRIFT EXEMPT (tracked) ---
  ':!DEVELOPER.md'
  ':!PROJECTS/SFW_PROJECT_SOLUTIONS/offer/PRICING_AND_VALUE_GUIDE.md'
  ':!PROJECTS/SFW_PROJECT_SOLUTIONS/offer/SME_AI_AUDIT_FUNNEL.md'
  ':!PROJECTS/SFW_PROJECT_SOLUTIONS/proposals/IMPLEMENTATION_PROPOSAL_TEMPLATE.md'
  ':!PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/NO_CODE_DELIVERY_PLANS/02_SME_AI_AUTOMATION_AUDIT_DELIVERY_PLAN.md'
  ':!PROJECTS/SFW_PROJECT_SOLUTIONS/delivery/NO_CODE_DELIVERY_PLANS/04_RELATIONSHIP_CONNECTOR_MODE_DELIVERY_PLAN.md'
)

# Lines containing any of these phrases are treated as "negation
# context" and skipped from drift hits, e.g. "Never use old Axis Live
# pricing".
NEGATION_REGEX='([Oo]ld |[Ss]uperseded|[Dd]o not use|[Nn]ever use|[Rr]eplaced by|[Ll]egacy|[Hh]istoric|[Nn]ot active|[Pp]reviously )'

# Superseded pricing phrases.
# £9,995 is intentionally NOT here because it is also a current
# Bundle Launch tier in PRICING_AUTHORITY.md.
SUPERSEDED_PHRASES=(
  '£497'
  '£997'
  '£5,595'
  '£4,995'
  '£3,195'
  'GBP 497'
  'GBP 997'
  'GBP 5,595'
  'GBP 4,995'
  'GBP 3,195'
  'Axis OS Live'
  'Axis Live\b'
  'Custom Axis OS Deployment'
)

fail=0

scan() {
  local label="$1"; shift
  local pattern="$1"; shift
  local raw filtered
  raw=$(git ls-files -z -- '*.md' "${EXCLUDES[@]}" \
    | xargs -0 grep -nE -- "$pattern" 2>/dev/null || true)
  if [ -z "$raw" ]; then return 0; fi
  filtered=$(echo "$raw" | grep -vE -- "$NEGATION_REGEX" || true)
  if [ -n "$filtered" ]; then
    echo "::error::$label drift detected for pattern: $pattern"
    echo "$filtered"
    fail=1
  fi
}

echo "== Scanning for superseded pricing =="
for p in "${SUPERSEDED_PHRASES[@]}"; do
  scan "Superseded pricing" "$p"
done

if [ "$fail" -ne 0 ]; then
  echo
  echo "Drift guard FAILED. See ::error:: lines above."
  echo "If a hit is legitimate (historical, audit, or archive), move the file"
  echo "into an excluded path or extend EXCLUDES in this script."
  echo "If it is real drift, fix the wording with reference to"
  echo "business/PRICING_AUTHORITY.md."
  exit 1
fi

echo "Drift guard OK."
