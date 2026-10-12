"""Службовий файл завдання 05. Не змінюйте його: ви редагуєте файли в папці task_05/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_05"
FILES = ['ufw.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 05) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
