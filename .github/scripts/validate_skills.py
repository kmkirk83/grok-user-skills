#!/usr/bin/env python3
"""
Validate Grok / Agent Skills against skill-creator and Agent Skills conventions.
Best-practice checks used by top-level skill repository maintainers.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("::error::PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

# Rules derived from skill-creator and common Agent Skills best practices
NAME_RE = re.compile(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$")
MAX_NAME_LEN = 64
MIN_NAME_LEN = 2
MAX_DESC_LEN = 1024
FORBIDDEN_IN_DESC = [": ", "<", ">"]  # colon-space and angle brackets banned in description


def error(msg: str, file: str | None = None) -> None:
    if file:
        print(f"::error file={file}::{msg}")
    else:
        print(f"::error::{msg}")


def warning(msg: str, file: str | None = None) -> None:
    if file:
        print(f"::warning file={file}::{msg}")
    else:
        print(f"::warning::{msg}")


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"Missing SKILL.md in {skill_dir.name}/")
        return errors

    content = skill_md.read_text(encoding="utf-8")
    if not content.startswith("---"):
        errors.append(f"{skill_md}: must start with YAML frontmatter (---)")
        return errors

    # Split frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        errors.append(f"{skill_md}: incomplete YAML frontmatter")
        return errors

    try:
        front = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        errors.append(f"{skill_md}: invalid YAML frontmatter: {e}")
        return errors

    if not isinstance(front, dict):
        errors.append(f"{skill_md}: frontmatter must be a mapping")
        return errors

    # Required fields
    name = front.get("name")
    description = front.get("description")

    if not name or not isinstance(name, str):
        errors.append(f"{skill_md}: missing or invalid 'name' field")
    else:
        if not (MIN_NAME_LEN <= len(name) <= MAX_NAME_LEN):
            errors.append(f"{skill_md}: name length must be {MIN_NAME_LEN}-{MAX_NAME_LEN}")
        if not NAME_RE.match(name):
            errors.append(
                f"{skill_md}: name must be kebab-case (lowercase letters, digits, single hyphens), start/end with alnum"
            )
        if name != skill_dir.name:
            errors.append(
                f"{skill_md}: directory name '{skill_dir.name}' must equal skill name '{name}'"
            )

    if not description or not isinstance(description, str):
        errors.append(f"{skill_md}: missing or invalid 'description' field")
    else:
        if len(description) > MAX_DESC_LEN:
            errors.append(f"{skill_md}: description exceeds {MAX_DESC_LEN} characters")
        for bad in FORBIDDEN_IN_DESC:
            if bad in description:
                errors.append(
                    f"{skill_md}: description must not contain '{bad}' (skill-creator rule)"
                )
        if description.strip().startswith("TODO") or "TODO —" in description:
            errors.append(f"{skill_md}: description still contains TODO placeholder")

    # Body quality checks
    body = parts[2].strip()
    if not body:
        errors.append(f"{skill_md}: empty body after frontmatter")
    if "TODO —" in body or "TODO:" in body:
        warning(f"{skill_md}: body contains TODO markers", str(skill_md))

    # Allowed top-level frontmatter keys (strict-ish)
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    extra = set(front.keys()) - allowed
    if extra:
        warning(
            f"{skill_md}: unexpected frontmatter keys {sorted(extra)} "
            "(prefer putting custom fields under metadata:)",
            str(skill_md),
        )

    return errors


def main() -> int:
    root = Path(".")
    # Discover skill directories (any dir containing SKILL.md at top level of that dir)
    skill_dirs = sorted(
        p.parent for p in root.rglob("SKILL.md") if p.parent != root and p.parent.parent == root
    )
    # Also support nested if needed, but for this repo they are top-level
    if not skill_dirs:
        # Fallback: any immediate subdir with SKILL.md
        skill_dirs = sorted(
            d for d in root.iterdir() if d.is_dir() and (d / "SKILL.md").is_file()
        )

    if not skill_dirs:
        error("No skill directories found (expected */SKILL.md)")
        return 1

    print(f"Found {len(skill_dirs)} skill(s): {', '.join(d.name for d in skill_dirs)}")
    print()

    all_errors: list[str] = []
    for skill_dir in skill_dirs:
        errs = validate_skill(skill_dir)
        if errs:
            for e in errs:
                error(e, str(skill_dir / "SKILL.md"))
                all_errors.append(e)
        else:
            print(f"✅ {skill_dir.name}")

    print()
    if all_errors:
        print(f"::error::{len(all_errors)} validation error(s) found")
        # Write summary for GITHUB_STEP_SUMMARY
        summary = os.environ.get("GITHUB_STEP_SUMMARY")
        if summary:
            with open(summary, "a", encoding="utf-8") as f:
                f.write("## Skill Validation Failed\n\n")
                for e in all_errors:
                    f.write(f"- {e}\n")
        return 1

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write("## Skill Validation Passed\n\n")
            f.write(f"Validated **{len(skill_dirs)}** skills successfully.\n")
    print(f"✅ All {len(skill_dirs)} skills passed validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
