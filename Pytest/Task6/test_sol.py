import pytest
from solution import is_prime
from math import sqrt
from random import randint
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

class TestMini:
    @pytest.mark.parametrize("input, output", [(-2, False), (0, False), (1, False), (3, True), (5, True)])
    def testy(self, input, output):
        assert is_prime(input) == output

t = [randint(10**4, 10**6) for _ in range(5)]
class TestMed:
    @pytest.mark.parametrize("input, output", [(t[i], my_prime(t[i])) for i in range(5)])
    def testy(self, input, output):
        assert is_prime(input) == output

t2 = [randint(10**12, 10**13) for _ in range(5)]
class TestMax:
    @pytest.mark.parametrize("input, output", [(t2[i], my_prime(t2[i])) for i in range(5)])
    def testy(self, input, output):
        assert is_prime(input) == output
