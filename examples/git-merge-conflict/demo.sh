#!/usr/bin/env bash
set -euo pipefail

demo_root=$(mktemp -d)
trap 'rm -rf -- "$demo_root"' EXIT

cd "$demo_root"
git init --quiet --initial-branch=main
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
