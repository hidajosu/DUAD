import pytest
from ejercicio1 import bubble_sort

def test_small_list():
    nums = [3, 1, 2]
    bubble_sort(nums)
    assert nums == [1, 2, 3]

def test_large_list():
    nums = list(range(200, 0, -1))
    bubble_sort(nums)
    assert nums == list(range(1, 201))

def test_empty_list():
    nums = []
    bubble_sort(nums)
    assert nums == []

def test_non_list_param():
    with pytest.raises(TypeError):
        bubble_sort("not a list")