import pytest
from cmplex import C
from random import randint

def testa():
    assert C(0, 0) * C(420, 420) == C(0, 0)

def testb():
    assert C(1, 1) * C(4, 1) == C(3, 5)

def testc():
    assert C(-2, 1) * C(5, 2) == C(-12, 1)

def testd():
    assert C(4, -2) * C(-1, 2) == C(0, 10)

def teste():
    x1 = randint(10**5, 10**10)
    x2 = randint(10**5, 10**10)
    y1 = randint(10**5, 10**10)
    y2 = randint(10**5, 10**10)
    assert C(x1, y1) * C(x2, y2) == C(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)