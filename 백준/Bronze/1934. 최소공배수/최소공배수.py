T = int(input())

# 최대공약수
def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

# 최소공배수
def lcm(x, y):
    res = (x*y)/gcd(x, y)
    return res

for i in range(T):
    ans = -1
    A, B = map(int, input().split())
    ans = lcm(A, B)
    print(int(ans))
    
    