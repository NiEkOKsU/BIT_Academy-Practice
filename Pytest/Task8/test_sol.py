import pytest
from sol import smallest_primeNum_bigger_than
from random import randint
from math import sqrt

def my_prime(x):

    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    tmp = 5

    while int(sqrt(x)) + 1 > tmp:
        if x % tmp == 0:
            return False
        tmp += 2
        if x % tmp == 0:
            return False
        tmp += 4
    
    return True

def my_f(n):

    if n % 2 == 0:
        n += 1
    else:
        n += 2

    while not my_prime(n):
        n += 2

    return n
ranges = [(0, 10), (0, 10), (-10, 10), (-10, 10), (0, 10**3), (0, 10**5), (0, 10**7), (0, 10**8), (-10, 10**13), (-10, 10**13), (-10*2, 10**15), (-10**4, 10**15)]

nums = [randint(ranges[i][0], ranges[i][1]) for i in range(len(ranges))]

@pytest.mark.parametrize("input, output", [(nums[i], my_f(nums[i])) for i in range(4)])
class TestMini:
    def tests(self, input, output):
        assert smallest_primeNum_bigger_than(input) == output

@pytest.mark.parametrize("input, output", [(nums[i], my_f(nums[i])) for i in range(4, 8)])
class TestMed:
    def tests(self, input, output):
        assert smallest_primeNum_bigger_than(input) == output

@pytest.mark.parametrize("input, output", [(nums[i], my_f(nums[i])) for i in range(8, 12)])
class TestMaxi:
    def tests(self, input, output):
        assert smallest_primeNum_bigger_than(input) == output