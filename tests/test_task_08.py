"""Автоматична перевірка завдання 08."""
import pytest
from conftest import load
from kits import mkr

V = load(8)
CASES = [{'id': 'копія з ротацією',
  'public': True,
  'kind': 'backup',
  'args': ['shop', 'bk', '3'],
  'files': {'bk/shop-20250101.dump': 'DUMP',
            'bk/shop-20250102.dump': 'DUMP',
            'bk/shop-20250103.dump': 'DUMP'},
  'now': '2025-01-15 10:00:00',
  'stdout': 'OK bk/shop-20250115.dump\n',
  'code': 0,
  'listing': {'bk': ['shop-20250115.dump', 'shop-20250103.dump', 'shop-20250102.dump']}},
 {'id': 'збій pg_dump',
  'public': True,
  'kind': 'backup',
  'args': ['shop', 'bk', '1'],
  'env': {'FAIL_DUMP': '1'},
  'now': '2025-01-15 10:00:00',
  'stdout': '',
  'code': 1,
  'stderr_contains': 'Помилка: pg_dump не вдався',
  'listing': {'bk': []}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_08(case):
    mkr.check(V, case)
