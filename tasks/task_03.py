"""Службовий файл завдання 03. Не змінюйте його: ви редагуєте файли в папці task_03/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_03"
FILES = ['task.service', 'task.timer']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 03) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
