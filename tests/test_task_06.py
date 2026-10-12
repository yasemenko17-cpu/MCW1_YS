"""Автоматична перевірка завдання 06."""
import pytest
from conftest import load
from kits import mkr

V = load(6)
CASES = [{'id': 'редирект з http',
  'public': True,
  'kind': 'nginx',
  'scheme': 'http',
  'host': 'shop.lab.test',
  'path': '/cart',
  'expect': {'kind': 'redirect', 'code': 301, 'location': 'https://shop.lab.test/cart'}},
 {'id': 'перевірка стану',
  'public': True,
  'kind': 'nginx',
  'scheme': 'https',
  'host': 'shop.lab.test',
  'path': '/health',
  'expect': {'kind': 'return', 'code': 200, 'body': 'ok'}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_06(case):
    mkr.check(V, case)
