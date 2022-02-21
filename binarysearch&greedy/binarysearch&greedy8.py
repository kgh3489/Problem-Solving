#침몰하는 타이타닉(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

'''
#기본적인 방법:

n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
cnt=0

while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.pop(0)
        p.pop()
        cnt+=1

print(cnt)
'''

#deque를 활용한 효울적인 방법(연산을 줄임)

from collections import deque

n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort() #맨 앞과 맨 뒤의 사람을 더하기 위해 정렬
p=deque(p) #자료구조를 큐로 선언
cnt=0

while p:
    if len(p)==1: #한 명만 남아있다면
        cnt+=1
        break
    if p[0]+p[-1]>limit: #제한을 초과하면
        p.pop() #제일 무거운 사람만 보트에 태움
        cnt+=1
    else: #제한보다 적거나 같다면
        #두 사람을 모두 보트에 태움
        p.popleft() 
        p.pop()
        cnt+=1
        
print(cnt)
