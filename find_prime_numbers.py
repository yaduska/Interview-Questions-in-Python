import math

def is_prime(no):
    if no < 2:
        return False
    if no == 2:
        return True
    if no % 2 == 0:
        return False

    square_root = math.isqrt(no)
    for a in range(3, square_root + 1, 2):
        if no % a == 0:
            return False

    return True

print(is_prime(29))

            
    
    