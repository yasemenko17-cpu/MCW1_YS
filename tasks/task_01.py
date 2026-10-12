"""Службовий файл завдання 01. Не змінюйте його: ви редагуєте файли в папці task_01/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_01"
FILES = ['task.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 01) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
