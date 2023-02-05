# 조합 구하기

# import sys
# sys.stdin=open("input.txt", "r")

def DFS(L, start):
    global total
    
    if L == M:
        for i in range(M):
            print(res[i], end= " ")
        print()
        total += 1
        return
    else:
        for i in range(start, N+1):
            res[L] = i
            DFS(L+1, i+1)
    
N, M = map(int, input().split())
res = [0] * N
total = 0
DFS(0, 1)
print(total)
