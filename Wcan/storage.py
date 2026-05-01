#Zapis JSON
# zapis JSON
import json
from datetime import datetime
from pathlib import Path

DATA_DIR = Path("data")
SCANS_DIR = DATA_DIR / "scans"


def ensure_scans_dir():
    SCANS_DIR.mkdir(parents=True, exist_ok=True)


def save_scan(scan):
    ensure_scans_dir()

    scan_id = scan["scan_id"]
    file_path = SCANS_DIR / f"scan_{scan_id}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(scan, file, indent=4, ensure_ascii=False)

    return file_path


def create_scan_object(target, results, ports_checked=None):
    if ports_checked is None:
        ports_checked = []

    scan_id = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    hosts_up = 0

    for result in results:
        if result["status"] == "up":
            hosts_up += 1

    scan = {
        "scan_id": scan_id,
        "target": target,
        "created_at": created_at,
        "devices": results,
        "summary": {
            "hosts_scanned": len(results),
            "hosts_up": hosts_up,
            "ports_checked": ports_checked
        }
    }

    return scan