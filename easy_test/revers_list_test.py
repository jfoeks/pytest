import pytest

@pytest.mark.parametrize("list1,list2",[
    ([1,2,3],[3,2,1]),
    ([2,7,12],[12,7,2]),
    ([5,12,32],[32,12,5]),
    ([5, 2, 3], [3, 2, 5]),
    ([21, 7, 122], [122, 7, 21]),
    ([54, 12, 52], [52, 12, 54])
])
def test_revers(list1,list2):
    assert revers_list(list1) == list2


def revers_list(lst):
    return(lst[::-1])