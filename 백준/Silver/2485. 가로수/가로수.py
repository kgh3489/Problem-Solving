import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
trees = []
gaps = []
for i in range(n):
    trees.append(int(input()))
    if i > 0:
        gaps.append(trees[i] - trees[i-1])

# 최대공약수 구하는 gcd 함수 이용
max_gap = gcd(gaps[0], gaps[1])
for i in range(1, n-1):
    max_gap = gcd(max_gap, gaps[i])     # 최대공약수 갱신

# 두 나무 사이 가장 긴 거리를 간격으로 나눈 몫 + 1이 전체 나무 수
# 놓을 수 있는 전체 나무 수 - 주어진 나무 수 n을 빼주면 심어야하는 나무 수
print((trees[-1]-trees[0]) // max_gap + 1 - n)