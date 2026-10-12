"""Службовий файл завдання 06. Не змінюйте його: ви редагуєте файли в папці task_06/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_06"
FILES = ['nginx.conf']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 06) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
