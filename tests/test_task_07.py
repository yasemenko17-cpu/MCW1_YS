"""Автоматична перевірка завдання 07."""
import pytest
from conftest import load
from kits import mkr

V = load(7)
CASES = [{'id': 'app_rw з підмережі застосунків',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'shop',
  'user': 'app_rw',
  'ip': '10.20.1.7',
  'expect': 'scram-sha-256'},
 {'id': 'app_rw з чужої адреси',
  'public': True,
  'kind': 'hba',
  'conn': 'host',
  'db': 'shop',
  'user': 'app_rw',
  'ip': '192.0.2.1',
  'expect': 'reject'}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_07(case):
    mkr.check(V, case)
