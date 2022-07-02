from plain_data import plain_data
import pytest

def test_use_case_1():
    result = plain_data([[1,2],[3,4]])
    assert result == [1,2,3,4]


def test_use_case_2():
    result = plain_data([1, [2, [3, [4, 5]]]])
    assert result == [1, 2, 3, 4, 5]

def test_use_case_3():
    result = plain_data([6, [1, [2, 3], 4], 5])
    assert result == [6, 1, 2, 3, 4, 5]

def test_use_case_4():
    result = plain_data([[[1, 2,], 3], 4, 5])
    assert result == [1, 2, 3, 4, 5]