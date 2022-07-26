import sys

N = int(input())
A = []
for _ in range(N):
    A.append(int(sys.stdin.readline()))
A.sort()
for i in A:
    print(i)