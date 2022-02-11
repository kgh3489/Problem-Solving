#뮤직비디오(결정 알고리즘)

#import sys
#sys.stdin=open("input.txt", "r")

def Count(capacity):
    cnt=1 #dvd 개수
    sum=0 #노래를 더한 시간
    for x in Music:
        if sum+x>capacity: #노래를 더한 시간이 용량보다 크다면
            cnt+=1 #dvd 개수 증가
            sum=x
        else:
            sum+=x
    return cnt

n, m=map(int, input().split())
Music=list(map(int, input().split()))

maxx=max(Music) #dvd용량은 노래 하나의 길이보단 커야 됨
lt=1 #최소: 합은 0이상
rt=sum(Music) #최대: Music의 모든 합
res=0

while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and Count(mid)<=m: #mid용량보다 m이 크다면
        res=mid
        rt=mid-1
    else:
        lt=mid+1
        
print(res)

