import pytest

@pytest.mark.parametrize("num1,num2",[
    (1,-1),
    (2,-2),
    (3,-3),
    (4,-4),
    (52,-52),
    (-52,52)
])
def test_revers(num1,num2):
    assert revers_number(num1) == num2


def revers_number(num):
    return(-num)