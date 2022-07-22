import pytest
from function import square
from random import randint

class testFirst:
    def testa(self):
        x = randint(-10, 10)
        assert square(x) == x ** 2

    def testb(self):
        x = randint(-10, 10)
        assert square(x) == x ** 2

    def testc(self):
        x = randint(-10, 10)
        assert square(x) == x ** 2

class testSecond:
    def testa(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

    def testb(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

    def testc(self):
        x = randint(-1000, 1000)
        assert square(x) == x ** 2

class testThird:
    def testa(self):
        x = randint(10 ** 4, 10 ** 6)
        assert square(x) == x ** 2
        
    def testb(self):
        x = randint(10 ** 4, 10 ** 6)
        assert square(x) == x ** 2

    def testc(self):
        x = randint(10 ** 4, 10 ** 6)
        assert square(x) == x ** 2

@pytest.mark.skipif(testThird.testa == pytest.fail or testThird.testb == pytest.fail or testThird.testc == pytest.fail)

class testFourth:
    def testa(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

    def testb(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

    def testc(self):
        x = randint(10 ** 12, 10 ** 13)
        assert square(x) == x ** 2

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie