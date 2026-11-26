from pathlib import Path
from tempfile import TemporaryDirectory

with TemporaryDirectory() as folder:
    path = Path(folder) / "notes.txt"
    path.write_text("فایل‌های پایتون کاربردی هستند.\n", encoding="utf-8")
    content = path.read_text(encoding="utf-8")
    print(content.strip())
