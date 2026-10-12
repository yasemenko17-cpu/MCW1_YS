"""Службовий файл завдання 09. Не змінюйте його: ви редагуєте файли в папці task_09/."""
from pathlib import Path

DIR = Path(__file__).resolve().parent / "task_09"
FILES = ['keys.sh', 'sshd_hardening.conf', 'ufw.sh']
for _name in FILES:
    if "TODO: реалізуйте" in (DIR / _name).read_text(encoding="utf-8"):
        raise NotImplementedError(f"Файл {_name} (завдання 09) ще не реалізовано: виконайте завдання за карткою і приберіть позначку TODO")
