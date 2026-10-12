"""Автоматична перевірка завдання 04."""
import pytest
from conftest import load
from kits import mkr

V = load(4)
CASES = [{'id': 'два найактивніші',
  'public': True,
  'kind': 'script',
  'args': ['log', '2'],
  'files': {'log': '10.0.0.2 - a\n10.0.0.1 - b\n10.0.0.2 - c\n10.0.0.3 - d\n10.0.0.2 - e\n10.0.0.1 - f\n'},
  'stdout': '3 10.0.0.2\n2 10.0.0.1\n',
  'code': 0},
 {'id': 'адрес менше за N',
  'public': True,
  'kind': 'script',
  'args': ['log', '5'],
  'files': {'log': 'a x\nb y\na z\n'},
  'stdout': '2 a\n1 b\n',
  'code': 0}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_04(case):
    mkr.check(V, case)
