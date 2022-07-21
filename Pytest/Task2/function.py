from math import sqrt
'''
def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, x):
        if not x % i:
            return False
    return True
'''
def is_prime(x):
    if x == 0 or x == 1:
        return False
    tmp = 2
    while tmp < int(sqrt(x)) + 1:
        if x % tmp == 0:
            return False
        tmp += 1
    return True