#공주 구하기(큐)

#import sys
#sys.stdin=open("input.txt", "r")

from collections import deque

n, k=map(int, input().split())
dq=list(range(1, n+1))
dq=deque(dq) #deque 자료구조료 변경

while dq: #dq가 비어있지 않다면
    for _ in range(k-1): 
        cur=dq.popleft() #맨 왼쪽의 수를 빼서
        dq.append(cur) #맨 오른쪽에 붙임
    dq.popleft() #k번째에 나온 수는 제거
    
    if len(dq)==1: #왕자가 한 명 남았을 때
        print(dq[0])
        dq.popleft()
