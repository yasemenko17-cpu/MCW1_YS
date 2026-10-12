"""Службовий файл завдання 10. Не змінюйте його: ви редагуєте файли в папці task_10/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_10"
FILES = ['domain.xml', 'network.xml', 'vm.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 10) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
