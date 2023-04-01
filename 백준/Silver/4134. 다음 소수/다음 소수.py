import sys
import math

input = sys.stdin.readline

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

T = int(input())
for i in range(T):
    z = int(input())
    while True:
        if is_prime(z):
            print(z)
            break
        else:
            z += 1
