#수들의 합

#import sys
#sys.stdin=open("input.txt", "r")

n, m=map(int, input().split())
a=list(map(int, input().split()))

lt=0 #lt는 a[0]에서 출발
rt=1 #rt는 a[1]에서 출발
tot=a[0] #lt에서 rt-1까지의 합
cnt=0

while True:
    if tot<m: #합이 m보다 작다면
        if rt<n:
            tot+=a[rt] #현재 rt를 더하
            rt+=1 #rt 위치 하나 증가
        else: #rt가 n까지 온다면
            break
    elif tot==m: #합이 m이라면
        cnt+=1
        tot-=a[lt] #현재 lt의 값을 빼고
        lt+=1 #lt 위치 하나 증가
    else: #합이 m보다 크다면
        tot-=a[lt] #현재 lt의 값을 빼고
        lt+=1 #lt 위치 하나 증가
print(cnt)
