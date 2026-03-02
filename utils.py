
def lcm(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    # gcd inline to avoid dependency
    x, y = a, b
    while y:
        x, y = y, x % y
    return a // x * b

