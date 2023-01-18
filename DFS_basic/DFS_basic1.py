# 재귀함수를 이용한 이진수 출력

# import sys
# sys.stdin=open("input.txt", "r")

def DFS(x):
    if x==0: # 0이면 종료
        return
    else:
        DFS(x//2)
        print(x%2, end='') # 나머지로 이진수를 만듦

n=int(input())
DFS(n)
