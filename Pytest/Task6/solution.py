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