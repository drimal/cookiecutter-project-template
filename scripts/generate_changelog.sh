#!/usr/bin/env bash
set -euo pipefail

# scripts/generate_changelog.sh
# Generate release notes for a tag, prepend to CHANGELOG.md, commit and push the change.
# Usage: ./scripts/generate_changelog.sh <tag>

TAG=${1:-}
if [ -z "$TAG" ]; then
  echo "Usage: $0 <tag>"
  exit 2
fi

echo "Generating changelog for $TAG"

LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || true)
if [ -n "$LAST_TAG" ] && [ "$LAST_TAG" != "$TAG" ]; then
  COMMIT_RANGE="$LAST_TAG..$TAG"
else
  COMMIT_RANGE="$TAG"
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
git --no-pager diff --name-only ${LAST_TAG:-} $TAG | sed 's/^/- /' | sed -n '1,80p' >> "$TMP_NOTES"

# Prepend to CHANGELOG.md
if [ ! -f CHANGELOG.md ]; then
  echo "# CHANGELOG" > CHANGELOG.md
  echo >> CHANGELOG.md
fi

TMP_CHANGES=$(mktemp)
cat "$TMP_NOTES" > "$TMP_CHANGES"
echo >> "$TMP_CHANGES"
cat CHANGELOG.md >> "$TMP_CHANGES"
mv "$TMP_CHANGES" CHANGELOG.md

# Commit and push the updated changelog (requires write permission / PAT)
git add CHANGELOG.md
git commit -m "chore(release): add CHANGELOG entry for $TAG" || echo "No changes to commit"
git push origin HEAD

# Also expose the notes file for use by the workflow
echo "$TMP_NOTES"
cp "$TMP_NOTES" /tmp/release-notes-for-$TAG.md
echo "/tmp/release-notes-for-$TAG.md"
