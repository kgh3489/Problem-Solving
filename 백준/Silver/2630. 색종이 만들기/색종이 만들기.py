import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
    color = paper[x][y] # 첫 번째 요소의 색깔
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] : # 다른 색이 나오면 자름
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

solution(0,0,N)
print(result.count(0))
print(result.count(1))