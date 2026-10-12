"""Автоматична перевірка завдання 03."""
import pytest
from conftest import load
from kits import mkr

V = load(3)
CASES = [{'id': 'тип служби', 'public': True, 'kind': 'service', 'expect': {'Type': ['oneshot']}},
 {'id': 'розклад на кілька днів',
  'public': True,
  'kind': 'calendar',
  'start': '2025-01-15 10:00:00',
  'runs': ['2025-01-16 06:45:00', '2025-01-17 06:45:00']}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_03(case):
    mkr.check(V, case)
