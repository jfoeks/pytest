import pytest

@pytest.mark.parametrize("array,sum",[
    ([1,2,3],6),
    ([50,2],52),
    ([40,5,5,5,5],60),
    ([50, 50, 50], 150),
    ([], False),
    ([12,16,-2], 26)
])
def test_sum(array,sum):
    assert sum_array(array) == sum


def sum_array(array):
    return sum(array)