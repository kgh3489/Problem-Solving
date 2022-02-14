#마구간 정하기(결정 알고리즘)

#import sys
#sys.stdin=open("input.txt", "r")

def Count(len):
    cnt=1
    ep=Line[0]
    for i in range(1, n):
        if Line[i]-ep>=len: #최대 거리보다 멀다면
            cnt+=1
            ep=Line[i]
    return cnt

n, c=map(int, input().split())
Line=[] #수직선상의 마구간

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)
Line.sort()

lt=1 #최소 거리
rt=Line[n-1] #최대 거리(맨 끝)

while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=c:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
        
print(res)
