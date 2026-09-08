"""Exercise the demo against synthetic caller repositories and Git settings."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


DEMO = Path(__file__).resolve().parents[1] / "examples/git-merge-conflict/demo.sh"


class GitDemoTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="teaching-demo-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)

    def run_demo(self, **settings):
        result = subprocess.run(
            ["bash", str(DEMO)], cwd=self.root,
            env={**self.env, **settings}, capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("merge_result=conflict\n", result.stdout)
        self.assertIn("unmerged_status=UU plan.txt\n", result.stdout)
        self.assertIn("resolved_line=截止时间：周四 15:00\n", result.stdout)
        self.assertIn("merge_commit_parents=2\n", result.stdout)

    def test_clean_environment(self):
        self.run_demo()

    def test_sourcing_is_rejected_without_changing_caller(self):
        result = subprocess.run(
            ["bash", "-c", 'before=$-; source "$1"; result=$?; '
             'test "$result" -ne 0 && test "$GIT_DIR" = sentinel && test "$-" = "$before"',
             "demo-source-check", str(DEMO)],
            cwd=self.root, env={**self.env, "GIT_DIR": "sentinel"},
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_old_git_is_rejected_before_repository_commands(self):
        binaries = self.root / "bin"
        binaries.mkdir()
        fake_git = binaries / "git"
        marker = self.root / "git-mutated"
        fake_git.write_text(
            '#!/bin/sh\nif [ "$1" = --version ]; then\n'
            '  echo "git version 2.28.0"\n  exit 0\nfi\n'
            'printf unexpected > "$DEMO_TEST_GIT_MARKER"\nexit 1\n', encoding="utf-8",
        )
        fake_git.chmod(0o755)
        result = subprocess.run(
            ["bash", str(DEMO)], cwd=self.root,
            env={**self.env, "PATH": str(binaries) + os.pathsep + self.env["PATH"],
                 "DEMO_TEST_GIT_MARKER": str(marker)},
            capture_output=True, text=True, timeout=30,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Git 2.32 or newer", result.stderr)
        self.assertFalse(marker.exists())

    def test_caller_repository_and_index_remain_unchanged(self):
        caller = self.root / "caller"
        subprocess.run(
            ["git", "init", "--quiet", "--initial-branch=main", "--template=", str(caller)],
            env=self.env, check=True,
        )
        (caller / "keep.txt").write_text("caller data\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(caller), "add", "keep.txt"], env=self.env, check=True)

        def snapshot():
            return {str(p.relative_to(caller)): p.read_bytes()
                    for p in caller.rglob("*") if p.is_file()}

        before = snapshot()
        result = subprocess.run(
            ["bash", str(DEMO)], cwd=caller,
            env={**self.env, "GIT_DIR": str(caller / ".git"),
                 "GIT_WORK_TREE": str(caller), "GIT_INDEX_FILE": str(caller / ".git/index")},
            capture_output=True, text=True, timeout=30,
        )
        self.assertEqual(snapshot(), before, "demo changed the synthetic caller repository")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("merge_commit_parents=2\n", result.stdout)

    def test_global_signing_settings_are_ignored(self):
        config = self.root / "signing.gitconfig"
        config.write_text("[commit]\n\tgpgsign = true\n[gpg]\n\tprogram = false\n", encoding="utf-8")
        self.run_demo(GIT_CONFIG_GLOBAL=str(config))

    def test_environment_config_is_ignored(self):
        self.run_demo(
            GIT_CONFIG_COUNT="1", GIT_CONFIG_KEY_0="commit.gpgsign", GIT_CONFIG_VALUE_0="true",
            GIT_CONFIG_PARAMETERS="'gpg.program=false'",
        )

    def test_template_hook_is_not_executed(self):
        template = self.root / "template"
        hooks = template / "hooks"
        hooks.mkdir(parents=True)
        marker = self.root / "hook-ran"
        hook = hooks / "pre-commit"
        hook.write_text('#!/bin/sh\nprintf executed > "$DEMO_TEST_HOOK_MARKER"\nexit 1\n', encoding="utf-8")
        hook.chmod(0o755)
        result = subprocess.run(
            ["bash", str(DEMO)], cwd=self.root,
            env={**self.env, "GIT_TEMPLATE_DIR": str(template), "DEMO_TEST_HOOK_MARKER": str(marker)},
            capture_output=True, text=True, timeout=30,
        )
        self.assertFalse(marker.exists(), "demo executed a caller template hook")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
