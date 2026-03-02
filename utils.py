
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
def gcd(a, b):

def is_power_of_five(n):
    if n <= 0:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1

def is_even(n):
    return n % 2 == 0
