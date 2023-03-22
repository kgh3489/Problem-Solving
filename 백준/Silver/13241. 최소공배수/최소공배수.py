A, B = map(int, input().split())

# Greatest Common Divisor
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

# Least Common Multiple
def lcm(x, y):
    return x * y // gcd(x, y)

print(lcm(A, B))