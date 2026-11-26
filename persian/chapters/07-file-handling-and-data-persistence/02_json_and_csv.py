import csv
import json
from pathlib import Path
from tempfile import TemporaryDirectory

records = [{"name": "آوا", "score": 18}, {"name": "نوح", "score": 16}]
with TemporaryDirectory() as folder:
    root = Path(folder)
    json_path = root / "records.json"
    json_path.write_text(json.dumps(records, indent=2), encoding="utf-8")
    restored = json.loads(json_path.read_text(encoding="utf-8"))
    csv_path = root / "records.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "score"])
        writer.writeheader()
        writer.writerows(restored)
    print(len(restored), csv_path.exists())
