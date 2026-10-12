"""Автоматична перевірка завдання 05."""
import pytest
from conftest import load
from kits import mkr

V = load(5)
CASES = [{'id': 'ssh з офісу',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '192.0.2.15', 'port': 22},
  'expect': 'ALLOW'},
 {'id': 'ssh ззовні',
  'public': True,
  'kind': 'ufw',
  'packet': {'proto': 'tcp', 'src': '203.0.113.5', 'port': 22},
  'expect': 'DENY'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_05(case):
    mkr.check(V, case)
