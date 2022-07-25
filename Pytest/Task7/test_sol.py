import pytest
from solution import Node, linked_list_sort, tab2list, list2tab
from random import randint

test_list = [[2,3,1], [2, 2, 2], [1,9,6,2,1,3,7], [-1, -5, 4, 9, 18]]
n = [100, 200, 500, 1000, 2000, 3000, 4000, 5000]

for i in range(4):
    to_append = [randint(-10**4, 10**4) for _ in range(n[i])]
    test_list.append(to_append)

for i in range(4, 8):
    to_append = [randint(-10**10, 10**10) for _ in range(n[i])]
    test_list.append(to_append)

head_list = [tab2list(test_list[i]) for i in range(12)]

@pytest.mark.parametrize("input, output", [(head_list[i], sorted(test_list[i])) for i in range(4)])
class TestMini:
    def tests(self, input, output):
        h = linked_list_sort(input)
        assert list2tab(h) == output

@pytest.mark.parametrize("input, output", [(head_list[i], sorted(test_list[i])) for i in range(4, 8)])
class TestMed:
    def tests(self, input, output):
        h = linked_list_sort(input)
        assert list2tab(h) == output

@pytest.mark.parametrize("input, output", [(head_list[i], sorted(test_list[i])) for i in range(8, 12)])
class TestMaxi:
    def tests(self, input, output):
        h = linked_list_sort(input)
        assert list2tab(h) == output

