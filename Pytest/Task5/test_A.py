import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'

@pytest.mark.parametrize("test_input, expected_output", [("aabbc", [2, 2, 1]), ("abbccc", [1, 2, 3]), ("aaaa", [4, 0, 0]), ("", [0, 0, 0]), ("cbcbccccccbbccb", [0, 5, 10])])

def tests(test_input, expected_output):
    assert count_chars(test_input) == expected_output