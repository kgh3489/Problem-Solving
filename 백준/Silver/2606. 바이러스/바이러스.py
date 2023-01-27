import sys

input = sys.stdin.readline

def DFS(v):
    visited[v] = 1 #방문 표시
    for nx in graph[v]:
        if visited[nx] == 0:
            DFS(nx)

com = int(input()) # 컴퓨터의 수
conn =  int(input()) # 컴퓨터 쌍의 수
graph = [[] for i in range(com + 1)]
visited = [0]*(com + 1) #방문한 컴퓨터
for i in range(conn):
    a, b = map(int, input().split())
    #양방향 그래프
    graph[a] += [b]
    graph[b] += [a]

DFS(1)
print(sum(visited) - 1)
    
