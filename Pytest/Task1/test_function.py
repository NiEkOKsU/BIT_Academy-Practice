import pytest
from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100
def testA():
    assert square(0) == 0
def testB():
    assert square(1) == 1
def testC():
    assert square(-1) == 1
def testD():
    assert square(100) == 10000