"""Службовий файл завдання 08. Не змінюйте його: ви редагуєте файли в папці task_08/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_08"
FILES = ['backup.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 08) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
