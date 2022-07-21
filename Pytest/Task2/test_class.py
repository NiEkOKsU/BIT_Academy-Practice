import pytest
from function import is_prime
from math import sqrt
from random import randint
#Złożoność: O(logx)
def prime_num(x):

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

    def testa(self):
        assert is_prime(-1) == False

    def testb(self):
        assert is_prime(0) == False

    def testc(self):
        assert is_prime(1) == False

    def testd(self):
        assert is_prime(2) == True

    def teste(self):
        assert is_prime(3) == True

    def testf(self):
        assert is_prime(4) == False

    def testg(self):
        assert is_prime(5) == True

    def testh(self):
        assert is_prime(6) == False

class TestMid:
    def testa(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == prime_num(x)

    def testb(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == prime_num(x)

    def testc(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == prime_num(x)

    def testd(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == prime_num(x)

    def teste(self):
        x = randint(10**4, 10**5)
        assert is_prime(x) == prime_num(x)

class TestMaxi:
    def testa(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == prime_num(x)

    def testb(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == prime_num(x)

    def testc(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == prime_num(x)

    def testd(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == prime_num(x)

    def teste(self):
        x = randint(10**12, 10**13)
        assert is_prime(x) == prime_num(x)
