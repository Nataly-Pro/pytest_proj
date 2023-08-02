import pytest
from utils import arrs


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]

def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2

def test_get_index_under_zero(array_fixture):
    assert arrs.get(array_fixture, -1, "test") == "test"

def test_get_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")

@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3, 4], 1, None, [2, 3, 4]),
    ([1, 2, 3, 4], -6, 3, [1, 2, 3]),
    ([1, 2, 3, 4], -2, 3, [3]),
    ([], 1, None, [])
])

def test_slice(coll, start, end, expected):
    assert arrs.my_slice(coll, start, end) == expected
