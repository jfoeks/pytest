import pytest

@pytest.mark.parametrize("num,array",[
    (123,[3,2,1]),
    (2721,[1,2,7,2]),
    (52123,[3,2,1,2,5]),
    (523, [3, 2, 5]),
    (127221, [1,2,2,7, 2,1]),
    (452125, [5,2, 1,2, 5,4])
])
def test_sum(num,array):
    assert number_array(num) == array

#Учитывая случайное неотрицательное число, вы должны вернуть цифры этого числа в массиве в обратном порядке.
def number_array(num):
    num = str(num)
    res_array = [int(i) for i in num]
    return(res_array[::-1])