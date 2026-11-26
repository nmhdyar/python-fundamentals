from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    "02-conditions-and-loops",
    "03-data-structures",
    "04-functions",
    "05-modules-and-debugging",
    "06-object-oriented-programming",
    "07-file-handling-and-data-persistence",
    "08-testing-and-code-quality",
    "09-iterators-and-generators",
    "10-advanced-python-concepts",
    "11-project-structure-and-packaging",
]
REQUIRED_EN_SECTIONS = (
    "Overview", "Learning objectives", "Prerequisites", "Lessons",
    "Worked examples", "Common mistakes", "Practice", "Recap",
    "Self-check", "Glossary",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    checked = 0
    paired_files = 0
    for chapter in CHAPTERS:
        english_dir = ROOT / "english" / "chapters" / chapter
        persian_dir = ROOT / "persian" / "chapters" / chapter
        if not english_dir.is_dir() or not persian_dir.is_dir():
            fail(f"Missing paired chapter directory: {chapter}")
        english_files = {p.name for p in english_dir.glob("*.py")}
        persian_files = {p.name for p in persian_dir.glob("*.py")}
        if english_files != persian_files:
            fail(f"Lesson filename mismatch in {chapter}: EN-only={sorted(english_files-persian_files)}, FA-only={sorted(persian_files-english_files)}")
        if not english_files:
            fail(f"No runnable Python lessons found in {chapter}")
        for language_dir in (english_dir, persian_dir):
            readme = language_dir / "README.md"
            if not readme.is_file():
                fail(f"Missing chapter README: {readme.relative_to(ROOT)}")
            content = readme.read_text(encoding="utf-8")
            if language_dir.parts[-3] == "english":
                for section in REQUIRED_EN_SECTIONS:
                    if section not in content:
                        fail(f"{readme.relative_to(ROOT)} is missing section: {section}")
            for filename in sorted(english_files):
                script = language_dir / filename
                source = script.read_text(encoding="utf-8")
                compile(source, str(script), "exec")
                result = subprocess.run([sys.executable, str(script)], cwd=ROOT, capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    fail(f"Script failed: {script.relative_to(ROOT)}\\nstdout:\\n{result.stdout}\\nstderr:\\n{result.stderr}")
                checked += 1
        paired_files += len(english_files)
    practice_en = (ROOT / "english" / "PRACTICE.md").read_text(encoding="utf-8")
    practice_fa = (ROOT / "persian" / "PRACTICE.md").read_text(encoding="utf-8")
    for number in range(2, 12):
        prefix = f"CH{number:02d}-EX"
        ids_en = sorted(set(re.findall(rf"\\b{prefix}\\d{{2}}\\b", practice_en)))
        ids_fa = sorted(set(re.findall(rf"\\b{prefix}\\d{{2}}\\b", practice_fa)))
        if ids_en != ids_fa or len(ids_en) != 5:
            fail(f"Exercise IDs differ or are incomplete for chapter {number}: EN={ids_en}, FA={ids_fa}")
    print(f"PASS: {checked} Python lesson scripts compiled and executed.")
    print(f"PASS: {paired_files} paired lesson filenames match across chapters 02–11.")
    print("PASS: Chapters 02–11 each contain five matching practice IDs.")


if __name__ == "__main__":
    main()
