import pytest
from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2

def test_get_index_under_zero():
    assert arrs.get([1, 2, 3], -1, "test") == "test"

def test_get_out_of_range():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]

def test_slice_empty_coll():
    assert arrs.my_slice([], 1) == []

def test_slice_start_under_zero():
    assert arrs.my_slice([1, 2, 3, 4], -6, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -2, 3) == [3]
