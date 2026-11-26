from pathlib import Path

layout = {
    "src/app": ["__init__.py", "main.py", "services.py"],
    "tests": ["test_services.py"],
    "docs": ["README.md"],
}
for folder, filenames in layout.items():
    print(Path(folder).as_posix(), "->", ", ".join(filenames))
