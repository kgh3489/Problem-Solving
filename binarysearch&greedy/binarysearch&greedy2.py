#랜선 자르기(결정 알고리즘)

#import sys
#sys.stdin=open("input.txt", "r")

def Count(len): #새로 만든 랜선의 개수를 세는 함수
    cnt=0
    for x in Line:
        cnt+=x//len
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0

#가장 긴 랜선을 찾음
for _ in range(k): 
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp)

lt=1
rt=largest

while lt<=rt:
    mid=(lt+rt)//2 #찾는 랜선의 길이
    if Count(mid)>=n:
        res=mid
        lt=mid+1
    else:
        rt=mid-1
        
print(res)
