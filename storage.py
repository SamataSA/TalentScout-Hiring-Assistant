import json
from pathlib import Path

DATA_PATH = Path("data/candidates.json")
DATA_PATH.parent.mkdir(exist_ok=True)

def save_candidate(data):
    if DATA_PATH.exists():
        existing = json.loads(DATA_PATH.read_text())  
    else:
        existing = []

    existing.append(data)

    DATA_PATH.write_text(json.dumps(existing, indent=2))
