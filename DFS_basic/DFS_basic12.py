# 수열 추측하기 (itertools)

#import sys
import itertools as it
#sys.stdin=open("input.txt", "rt")

N, F = map(int, input().split())
b = [1] * n
cnt = 0
for i in range(1, n):
    b[i] = b[i-1]*(n-i)/i # 이항 계수
a = list(range(1, n+1))

for tmp in it.permutations(a): # 리스트 a에 있는 순열
    sum = 0
    for L, x in enumerate(tmp):
        sum += (x*b[L])
    if sum == F:
        for x in tmp:
            print(x, end=' ')
        break
