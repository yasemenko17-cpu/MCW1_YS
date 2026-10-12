"""Автоматична перевірка завдання 01."""
import pytest
from conftest import load
from kits import mkr

V = load(1)
CASES = [{'id': 'змішані права виправлено',
  'public': True,
  'kind': 'script',
  'args': ['d'],
  'files': {'d/a.conf': {'text': 'x', 'mode': 438},
            'd/b.sh': {'text': 'x', 'mode': 420},
            'd/c.txt': {'text': 'x', 'mode': 384}},
  'stdout': 'FIXED a.conf\nFIXED b.sh\nFIXED c.txt\nВиправлено: 3\n',
  'code': 0,
  'modes': {'d/a.conf': 416, 'd/b.sh': 488, 'd/c.txt': 420}},
 {'id': 'уже правильні права',
  'public': True,
  'kind': 'script',
  'args': ['d'],
  'files': {'d/a.conf': {'text': 'x', 'mode': 416}, 'd/b.sh': {'text': 'x', 'mode': 488}},
  'stdout': 'Виправлено: 0\n',
  'code': 0,
  'modes': {'d/a.conf': 416, 'd/b.sh': 488}}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_01(case):
    mkr.check(V, case)
