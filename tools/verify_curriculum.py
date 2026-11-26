from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = (
    "03-data-structures",
    "04-functions",
    "05-modules-and-debugging",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    checked = 0

    for chapter in CHAPTERS:
        english_dir = ROOT / "english" / "chapters" / chapter
        persian_dir = ROOT / "persian" / "chapters" / chapter
        if not english_dir.is_dir() or not persian_dir.is_dir():
            fail(f"Missing paired chapter directory: {chapter}")

        english_files = {p.name for p in english_dir.glob("*.py")}
        persian_files = {p.name for p in persian_dir.glob("*.py")}
        if english_files != persian_files:
            fail(
                f"English/Persian lesson mismatch in {chapter}: "
                f"English-only={sorted(english_files - persian_files)}, "
                f"Persian-only={sorted(persian_files - english_files)}"
            )

        for language_dir in (english_dir, persian_dir):
            readme = language_dir / "README.md"
            if not readme.is_file():
                fail(f"Missing chapter README: {readme.relative_to(ROOT)}")
            content = readme.read_text(encoding="utf-8")
            for section in ("Overview", "Learning objectives", "Prerequisites",
                            "Lessons", "Worked examples", "Common mistakes",
                            "Practice", "Recap", "Self-check", "Glossary"):
                if language_dir.parts[-3] == "english" and section not in content:
                    fail(f"{readme.relative_to(ROOT)} is missing section: {section}")

            for filename in sorted(english_files):
                script = language_dir / filename
                compile(script.read_text(encoding="utf-8"), str(script), "exec")
                result = subprocess.run(
                    [sys.executable, str(script)],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    timeout=10,
                )
                if result.returncode != 0:
                    fail(
                        f"Script failed: {script.relative_to(ROOT)}\\n"
                        f"stdout:\\n{result.stdout}\\nstderr:\\n{result.stderr}"
                    )
                checked += 1

    practice_en = (ROOT / "english" / "PRACTICE.md").read_text(encoding="utf-8")
    practice_fa = (ROOT / "persian" / "PRACTICE.md").read_text(encoding="utf-8")
    for chapter_number in (3, 4, 5):
        prefix = f"CH{chapter_number:02d}-EX"
        ids_en = sorted(set(re.findall(rf"\\b{prefix}\\d{{2}}\\b", practice_en)))
        ids_fa = sorted(set(re.findall(rf"\\b{prefix}\\d{{2}}\\b", practice_fa)))
        if ids_en != ids_fa or len(ids_en) != 5:
            fail(f"Exercise IDs differ or are incomplete for chapter {chapter_number}: "
                 f"EN={ids_en}, FA={ids_fa}")

    print(f"PASS: {checked} Python lesson scripts compiled and executed.")
    print("PASS: English/Persian lesson filenames match for chapters 03–05.")
    print("PASS: Chapters 03–05 each contain five paired practice IDs.")


if __name__ == "__main__":
    main()
