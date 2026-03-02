
def sum_digits(n: int) -> int:
    n = abs(n)
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

def lcm(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    # gcd inline to avoid dependency
    x, y = a, b
    while y:
        x, y = y, x % y
    return a // x * b

=======

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
