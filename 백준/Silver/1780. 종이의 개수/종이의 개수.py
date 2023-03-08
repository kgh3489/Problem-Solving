'''
2차원 리스트로 받음
첫 번째 숫자 확인
그 이후로 다른 수가 나오면 자름(9등분)
'''
import sys

input = sys.stdin.readline
        
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

ans = []

def solution(x, y, size):
    start = paper[x][y]

    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != start:
                for k in range(3):
                    for l in range(3):
                        solution(x + k*size//3, y + l*size//3, size//3)
                return

    ans.append(start)
        

solution(0, 0, N)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))
