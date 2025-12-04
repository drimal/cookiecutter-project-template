#!/usr/bin/env bash
set -euo pipefail

# Compute next semantic version tag based on commits since last tag.
# Heuristic:
# - If any commit contains "BREAKING CHANGE" or has a conventional-commit "!", bump major
# - Else if any commit subject starts with "feat", bump minor
# - Else bump patch

LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null || true)
if [ -z "$LAST_TAG" ]; then
  BASE="v0.1.0"
  echo "$BASE"
  exit 0
fi

COMMITS_RANGE="$LAST_TAG..HEAD"

MAJOR=false
MINOR=false

while read -r line; do
  # check for BREAKING CHANGE token anywhere in commit body
  if echo "$line" | grep -qE "BREAKING CHANGE|!\)"; then
    MAJOR=true
  fi
  # check subject starts with feat(
  if echo "$line" | sed -E 's/^\s*//' | grep -qE '^feat(\(|:|\b)'; then
    MINOR=true
  fi
done < <(git --no-pager log $COMMITS_RANGE --pretty=format:'%s%n%b')

semver_strip_v() {
  echo "$1" | sed -E 's/^v//'
}

inc_patch() {
  IFS=. read -r major minor patch <<<"$1"
  patch=$((patch + 1))
  echo "$major.$minor.$patch"
}

inc_minor() {
  IFS=. read -r major minor patch <<<"$1"
  minor=$((minor + 1))
  patch=0
  echo "$major.$minor.$patch"
}

inc_major() {
  IFS=. read -r major minor patch <<<"$1"
  major=$((major + 1))
  minor=0
  patch=0
  echo "$major.$minor.$patch"
}

base=$(semver_strip_v "$LAST_TAG")

if [ "$MAJOR" = true ]; then
  next=$(inc_major "$base")
elif [ "$MINOR" = true ]; then
  next=$(inc_minor "$base")
else
  next=$(inc_patch "$base")
fi

echo "v$next"
