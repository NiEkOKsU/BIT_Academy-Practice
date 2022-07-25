from math import sqrt

def is_prime(x):

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

def smallest_primeNum_bigger_than(n):

    if n % 2 == 0:
        n += 1
    else:
        n += 2

    while not is_prime(n):
        n += 2

    return n