# 중복순열 구하기

import sys

# sys.stdin=open("input.txt", "r")
input = sys.stdin.readline

def DFS(L):
    global cnt
    
    if L == M:
        print(*res) # 차례대로 순열 출력
        cnt += 1
    else:
        for i in range(1, N+1):
            res[L] = i
            DFS(L+1)

N, M = map(int, input().split())
res = [0] * M
cnt = 0 # 총 경우의 수
DFS(0)
print(cnt)
