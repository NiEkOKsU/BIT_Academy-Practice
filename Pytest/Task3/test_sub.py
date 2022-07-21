import pytest
from cmplex import C
from random import randint

def testa():
    assert C(3, 4) - C(0, 0) == C(3, 4)

def testb():
    assert C(-1, -1) - C(2, 4) == C(-3, -5)

def testc():
    assert C(10, 18) - C(10, 6) == C(0, 12)

def testd():
    assert C(0, 0) - C(-1, -2) == C(1, 2)

def teste():
    x1 = randint(10**5, 10**10)
    x2 = randint(10**5, 10**10)
    y1 = randint(10**5, 10**10)
    y2 = randint(10**5, 10**10)
    assert C(x1, y1) - C(x2, y2) == C(x1 - x2, y1 - y2)