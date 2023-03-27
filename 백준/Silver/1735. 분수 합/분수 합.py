a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d + c*b # 분모
f = b*d # 분자

# Greatest Common Divisor
def gcd(x, y):
    while y > 0:
        x, y = y, x%y
    return x

n = gcd(e, f) # 최대공약수
print(e//n, f//n)