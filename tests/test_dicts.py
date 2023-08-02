import pytest
from utils import dicts

def test_get_val():
    assert dicts.get_val({"vcs": "mercurial"}, "vcs") == "mercurial"
    assert dicts.get_val({"vcs": "mercurial"}, "vcs", "test") == "mercurial"
    assert dicts.get_val({}, "vcs", "test") == "test"

