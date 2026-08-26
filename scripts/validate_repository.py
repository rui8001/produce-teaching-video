#!/usr/bin/env python3
"""Validate the public Skill package without touching private production files."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_INTERFACE = {
    "display_name",
    "short_description",
    "icon_small",
    "icon_large",
    "brand_color",
    "default_prompt",
}
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return [ROOT / item.decode() for item in result.stdout.split(b"\0") if item]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def validate_skill(errors: list[str]) -> None:
    path = ROOT / "SKILL.md"
    if not path.is_file():
        errors.append("SKILL.md is missing")
        return

    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md has invalid YAML frontmatter boundaries")
        return

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"SKILL.md frontmatter is invalid YAML: {exc}")
        return

    if not isinstance(frontmatter, dict):
        errors.append("SKILL.md frontmatter must be a mapping")
        return

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER
    if unexpected:
        errors.append(f"SKILL.md has unsupported frontmatter keys: {sorted(unexpected)}")

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("SKILL.md name must be lowercase hyphen-case")
    elif len(name) > 64:
        errors.append("SKILL.md name exceeds 64 characters")
    elif name != ROOT.name:
        errors.append(f"SKILL.md name {name!r} does not match repository folder {ROOT.name!r}")

    if not isinstance(description, str) or not description.strip():
        errors.append("SKILL.md description is missing")
    elif len(description.strip()) > 1024:
        errors.append("SKILL.md description exceeds 1024 characters")
    elif "<" in description or ">" in description:
        errors.append("SKILL.md description contains angle brackets")

    if re.search(r"(?m)^\s*\[TODO:[^\n]*\]\s*$", text[match.end() :]):
        errors.append("SKILL.md contains an unfinished TODO placeholder")


def validate_openai_yaml(errors: list[str]) -> None:
    path = ROOT / "agents" / "openai.yaml"
    if not path.is_file():
        errors.append("agents/openai.yaml is missing")
        return

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        errors.append(f"agents/openai.yaml is invalid YAML: {exc}")
        return

    interface = data.get("interface") if isinstance(data, dict) else None
    if not isinstance(interface, dict):
        errors.append("agents/openai.yaml is missing the interface mapping")
        return

    missing = REQUIRED_INTERFACE - set(interface)
    if missing:
        errors.append(f"agents/openai.yaml is missing interface fields: {sorted(missing)}")

    for field in ("icon_small", "icon_large"):
        target = interface.get(field)
        if not isinstance(target, str) or not (ROOT / target).is_file():
            errors.append(f"agents/openai.yaml {field} does not point to an existing file")

    prompt = interface.get("default_prompt")
    if not isinstance(prompt, str) or "$produce-teaching-video" not in prompt:
        errors.append("agents/openai.yaml default_prompt must invoke $produce-teaching-video")

    policy = data.get("policy") if isinstance(data, dict) else None
    if not isinstance(policy, dict) or policy.get("allow_implicit_invocation") is not True:
        errors.append("agents/openai.yaml must preserve automatic invocation")


def validate_json(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("examples/**/*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)} is invalid JSON: {exc}")


def validate_svg(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("**/*.svg")):
        try:
            ET.parse(path)
        except ET.ParseError as exc:
            errors.append(f"{path.relative_to(ROOT)} is invalid XML/SVG: {exc}")


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    return target.split(maxsplit=1)[0]


def validate_markdown_links(errors: list[str]) -> None:
    for path in sorted(ROOT.glob("**/*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = normalize_link_target(match.group(1))
            parsed = urlparse(target)
            if not target or target.startswith("#") or parsed.scheme in {"http", "https", "mailto", "data"}:
                continue
            relative_target = unquote(target.split("#", 1)[0])
            if relative_target.startswith("/"):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} uses an absolute local link"
                )
                continue
            resolved = (path.parent / relative_target).resolve()
            if ROOT not in resolved.parents and resolved != ROOT:
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} links outside the repository"
                )
            elif not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, match.start())} has a broken link to {target}"
                )


def validate_sensitive_data(errors: list[str]) -> None:
    mac_user_prefix = "/" + "Users" + "/"
    patterns = [
        ("OpenAI-style API key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
        ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
        ("GitHub fine-grained token", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
        ("private key header", re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")),
        ("bearer credential", re.compile(r"Authorization:\s*Bearer\s+[A-Za-z0-9._~-]{12,}", re.I)),
        ("cookie value", re.compile(r"Cookie:\s*[^\s=;]+=[^\s;]{8,}", re.I)),
        ("personal macOS path", re.compile(re.escape(mac_user_prefix) + r"[^/\s]+/")),
    ]

    for path in tracked_files():
        if not path.is_file():
            continue
        raw = path.read_bytes()
        if b"\0" in raw:
            continue
        text = raw.decode("utf-8", errors="ignore")
        for label, pattern in patterns:
            match = pattern.search(text)
            if match:
                errors.append(
                    f"{label} pattern found in {path.relative_to(ROOT)}:{line_number(text, match.start())}"
                )


def main() -> int:
    errors: list[str] = []
    validate_skill(errors)
    validate_openai_yaml(errors)
    validate_json(errors)
    validate_svg(errors)
    validate_markdown_links(errors)
    validate_sensitive_data(errors)

    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Repository validation passed: Skill, metadata, examples, links, SVG, and sensitive-data checks are clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
