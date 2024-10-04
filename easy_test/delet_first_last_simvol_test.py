import pytest

@pytest.mark.parametrize("list1,list2",[
    ([1,2,3],[2]),
    ([2,7,12],[7]),
    ([5,12,32],[12]),
    ([3,2,5,5,4,2], [2,5,5,4]),
    ([21, 7, 122,2], [7, 122]),
    ([2,1], []),
    (['h','e','l','l','o'], ['e','l','l'])

])
def test_delet_simvol(list1,list2):
    assert delet_simvol(list1) == list2

@pytest.mark.parametrize("list1,list2",[
    ([1,2,3],[2]),
    ([2,7,12],[7]),
    ([5,12,32],[12]),
    ([3,2,5,5,4,2], [2,5,5,4]),
    ([21, 7, 122,2], [7, 122]),
    ([2,1], []),
    (['h','e','l','l','o'], ['e','l','l'])

])
def test_delet_simvol2(list1,list2):
    assert delet_simvol2(list1) == list2


#Удалить первый и последний символ массива
def delet_simvol(lst):
    lst.pop(0)
    lst.pop(-1)
    return(lst)

def delet_simvol2(lst):
    return(lst[1:-1])
