# 순열 구하기

# import sys
# sys.stdin=open("input.txt", "r")


def DFS(L):
    global total

    if L == M:
        print(*res)
        total += 1
        return
    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1 # 사용한 수 표시
                res[L] = beads[i]
                DFS(L+1)
                check[i] = 0 # 사용하지 않은 상태로 되돌림
            else: # 이미 사용한 수라면
                continue

    
N, M = map(int, input().split())
beads = [i+1 for i in range(N)]
check = [0] * N
res = [0] * M
total = 0
DFS(0)
print(total)
