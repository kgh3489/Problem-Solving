#침몰하는 타이타닉(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

from collections import deque

n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
cnt=0
while p:
    if len(p)==1:
        cnt+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        cnt+=1
    else:
        p.popleft()
        p.pop()
        cnt+=1
print(cnt)

