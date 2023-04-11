import sys

input = sys.stdin.readline

N = int(input())
rainbow = []

for _ in range(N):
    A, B = input().split()
    if A == "ChongChong" or B == "ChongChong":
        rainbow.append(A)
        rainbow.append(B)
    elif rainbow:
        if A in rainbow or B in rainbow:
            rainbow.append(A)
            rainbow.append(B)
            
print(len(set(rainbow)))