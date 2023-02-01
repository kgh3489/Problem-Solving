# 동전 교환

# import sys
# sys.stdin=open("input.txt", "r")

def DFS(L, sum):
    global total

    if L > total: # 최소 개수를 탐색하므로 
        return
    if total >= M:
        return
    if sum == M: # 거스름돈과 같다면
        if L < total:
            total = L
    else:
        for i in coins:
            DFS(L+1, sum+i)

N = int(input())
coins = list(map(int, input().split()))
M = int(input())

total = 501
coins.sort(reverse=True) # 단위가 큰 동전부터 사용하기 위해
DFS(0, 0)

