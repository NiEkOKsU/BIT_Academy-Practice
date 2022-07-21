import pytest
from cmplex import C
from random import randint

def testa():
    assert C(0, 0) == C(0, 0)

def testb():
    assert C(69, 2137) == C(69, 2137)

def testc():
    x = randint(10**5, 10**10)
    y = randint(10**5, 10**10)
    assert C(x, y) == C(x, y)