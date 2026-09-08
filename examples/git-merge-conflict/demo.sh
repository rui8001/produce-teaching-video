#!/usr/bin/env bash
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  printf 'Run this demo with bash; do not source it.\n' >&2
  return 1
fi
set -euo pipefail

# A temporary cwd alone does not override an inherited GIT_DIR or index.
# Keep repository selectors, config injection, signing and templates out of
# this subprocess without changing the caller's environment or Git settings.
for git_env_name in ${!GIT_@}; do
  unset "$git_env_name"
done
export GIT_CONFIG_NOSYSTEM=1
export GIT_CONFIG_GLOBAL=/dev/null
export GIT_TERMINAL_PROMPT=0

git_version=$(git --version)
version_pattern='^git version ([0-9]+)\.([0-9]+)'
if [[ ! "$git_version" =~ $version_pattern ]] ||
   (( BASH_REMATCH[1] < 2 || (BASH_REMATCH[1] == 2 && BASH_REMATCH[2] < 32) )); then
  printf 'This isolated demo requires Git 2.32 or newer.\n' >&2
  exit 1
fi

demo_root=$(mktemp -d)
trap 'rm -rf -- "$demo_root"' EXIT

cd "$demo_root"
git init --quiet --initial-branch=main --template=
git config core.hooksPath /dev/null
git config core.attributesFile /dev/null
git config core.excludesFile /dev/null
git config user.name "Demo User"
git config user.email "demo@example.invalid"

printf '会议主题：产品评审\n截止时间：周五 17:00\n' > plan.txt
git add plan.txt
git commit --quiet -m "Add meeting plan"

git switch --quiet --create feature
printf '会议主题：产品评审\n截止时间：周四 17:00\n' > plan.txt
git add plan.txt
git commit --quiet -m "Move review to Thursday"

git switch --quiet main
printf '会议主题：产品评审\n截止时间：周五 15:00\n' > plan.txt
git add plan.txt
git commit --quiet -m "Move review earlier"

set +e
merge_output=$(git merge feature 2>&1)
merge_exit=$?
set -e

if [[ $merge_exit -eq 0 ]]; then
  printf 'Expected a conflict, but merge succeeded.\n' >&2
  exit 1
fi

unmerged_status=$(git status --short)
if [[ "$unmerged_status" != "UU plan.txt" ]]; then
  printf 'Unexpected unmerged status: %s\n' "$unmerged_status" >&2
  exit 1
fi

for marker in '<<<<<<< HEAD' '=======' '>>>>>>> feature'; do
  if ! grep -Fq "$marker" plan.txt; then
    printf 'Missing expected conflict marker: %s\n' "$marker" >&2
    exit 1
  fi
done

printf '会议主题：产品评审\n截止时间：周四 15:00\n' > plan.txt
git add plan.txt

if [[ $(git status --short) != "M  plan.txt" ]]; then
  printf 'Resolved file was not staged as expected.\n' >&2
  exit 1
fi

GIT_EDITOR=true git merge --continue >/dev/null

read -r -a commit_fields <<<"$(git rev-list --parents --max-count=1 HEAD)"
if [[ ${#commit_fields[@]} -ne 3 ]]; then
  printf 'Expected a merge commit with two parents.\n' >&2
  exit 1
fi

printf 'merge_result=conflict\n'
printf 'unmerged_status=%s\n' "$unmerged_status"
printf 'conflict_markers=present\n'
printf 'resolved_line=%s\n' "$(sed -n '2p' plan.txt)"
printf 'merge_commit_parents=2\n'
