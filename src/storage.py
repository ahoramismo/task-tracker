import os
import json
from constants import TASKS_FILE, DEFAULT_DATA


def ensure_data_file(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    if not os.path.exists(file_path):
        save_json(DEFAULT_DATA)


def load_json(file_path):
    ensure_data_file(file_path)
    with open(file_path, "r") as f:
        return json.load(f)


# json dumps vs json dump?
def save_json(data, file_path=TASKS_FILE):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
