# 인접 행렬 (가중치 방향 그래프)

#import sys
#sys.stdin=open("input.txt", "r")

n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    ''' 무방향 그래프인 경우'''
    # a, b = map(int, input().split())
    # g[a][b] = 1
    # g[b][a] = 1
    ''' 방향 그래프인 경우'''
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()
