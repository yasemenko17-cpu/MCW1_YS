"""Автоматична перевірка завдання 09."""
import pytest
from conftest import load
from kits import mkr

V = load(9)
CASES = [{'id': 'адміністратор з підмережі',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '203.0.113.10', 'port': 2200},
  'expect': 'ALLOW'},
 {'id': 'заблокована адреса',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '203.0.113.66', 'port': 2200},
  'expect': 'DENY'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_09(case):
    mkr.check(V, case)
