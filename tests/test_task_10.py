"""Автоматична перевірка завдання 10."""
import pytest
from conftest import load
from kits import mkr

V = load(10)
CASES = [{'id': 'базовий образ',
  'public': True,
  'kind': 'vm',
  'images': {'base.qcow2': {'format': 'qcow2', 'virtual-size': 10737418240}}},
 {'id': "пам'ять домену", 'public': True, 'kind': 'domain', 'expect': {'memory_kib': 4194304}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_10(case):
    mkr.check(V, case)
