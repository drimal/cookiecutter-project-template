#!/usr/bin/env bash
set -euo pipefail

# scripts/release.sh
# Usage: ./scripts/release.sh <tag> [release-title]
# Example: ./scripts/release.sh v0.2.0 "v0.2.0"

TAG=${1:-}
TITLE=${2:-"$TAG"}

# If no tag supplied, attempt to compute next tag using commits
if [ -z "$TAG" ]; then
  if [ -x "scripts/compute_next_tag.sh" ]; then
    echo "No tag specified — computing next tag from commits"
    TAG=$(scripts/compute_next_tag.sh)
    TITLE="$TAG"
    echo "Computed tag: $TAG"
  else
    echo "Usage: $0 <tag> [release-title]" >&2
    exit 2
  fi
fi

# ensure we're on main and working tree clean
BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [ "$BRANCH" != "main" ]; then
  echo "Warning: releasing from branch '$BRANCH' (recommended: main)"
fi

if ! git diff-index --quiet HEAD --; then
  echo "Working tree is dirty — please commit or stash changes before releasing"
  exit 1
fi

# check tag existence
if git rev-parse -q --verify "refs/tags/$TAG" >/dev/null; then
  echo "Tag $TAG already exists. Aborting to avoid overwrite." >&2
  exit 1
fi

LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || true)

if [ -n "$LAST_TAG" ]; then
  COMMIT_RANGE="$LAST_TAG..HEAD"
else
  COMMIT_RANGE="HEAD"
fi

TMP_NOTES=$(mktemp)
trap 'rm -f "$TMP_NOTES"' EXIT

echo "# $TAG - $(date +%F)" > "$TMP_NOTES"
echo >> "$TMP_NOTES"
echo "Changes since ${LAST_TAG:-<initial>}" >> "$TMP_NOTES"
echo >> "$TMP_NOTES"
git --no-pager log $COMMIT_RANGE --pretty=format:'- %h %ad %s (%an)' --date=short >> "$TMP_NOTES"
echo >> "$TMP_NOTES"
echo "Files changed (selected)" >> "$TMP_NOTES"
echo >> "$TMP_NOTES"
git --no-pager diff --name-only ${LAST_TAG:-} HEAD | sed 's/^/- /' | sed -n '1,40p' >> "$TMP_NOTES"

# Prepend to CHANGELOG.md (create if missing)
if [ ! -f CHANGELOG.md ]; then
  echo "# CHANGELOG" > CHANGELOG.md
  echo >> CHANGELOG.md
fi

TMP_CHANGES=$(mktemp)
cat "$TMP_NOTES" > "$TMP_CHANGES"
echo >> "$TMP_CHANGES"
cat CHANGELOG.md >> "$TMP_CHANGES"
mv "$TMP_CHANGES" CHANGELOG.md

git add CHANGELOG.md
git commit -m "chore(release): add CHANGELOG entry for $TAG"

# create annotated tag
git tag -a "$TAG" -m "$TITLE"

# push commit and tag
git push origin HEAD
git push origin "$TAG"

# create or update GitHub release if gh is available
if command -v gh >/dev/null 2>&1; then
  gh release create "$TAG" --title "$TITLE" --notes-file "$TMP_NOTES" || \
    gh release edit "$TAG" --title "$TITLE" --notes-file "$TMP_NOTES"
  # upload CHANGELOG.md as an asset (clobber if exists)
  gh release upload "$TAG" CHANGELOG.md --clobber || true
  echo "GitHub release updated: $(gh release view "$TAG" --json url -q .url || true)"
else
  echo "gh CLI not found — pushed tag and changelog commit, but release was not created on GitHub"
fi

echo "Release $TAG created and CHANGELOG.md updated."
