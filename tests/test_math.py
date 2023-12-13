import pytest

def add_two_numbers(x, y):
    return x + y

@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1, 6) == 7, "The sum of 1 and 6 should be 7"

@pytest.mark.math
def test_large_numbers():
    assert add_two_numbers(100, 300) == 400, "The sum of 100 and 300 should be 400"
