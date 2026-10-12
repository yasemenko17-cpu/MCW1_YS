"""Автоматична перевірка завдання 02."""
import pytest
from conftest import load
from kits import mkr

V = load(2)
CASES = [{'id': 'звичайні користувачі з оболонкою',
  'public': True,
  'kind': 'script',
  'args': ['passwd'],
  'files': {'passwd': 'root:x:0:0::/root:/bin/bash\n'
                      'alice:x:1001:1001::/home/alice:/bin/bash\n'
                      'bob:x:1000:1000::/home/bob:/bin/zsh\n'},
  'stdout': 'bob\nalice\n',
  'code': 0},
 {'id': 'лише nologin та false',
  'public': True,
  'kind': 'script',
  'args': ['passwd'],
  'files': {'passwd': 'www:x:1000:1000::/var/www:/usr/sbin/nologin\nsvc:x:1001:1001::/srv:/bin/false\n'},
  'stdout': 'Немає\n',
  'code': 0}]


@pytest.mark.parametrize("case", CASES, ids=[c["id"] for c in CASES])
def test_task_02(case):
    mkr.check(V, case)
