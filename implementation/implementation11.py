#점수 계산

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))
sum=0
cnt=0

for x in a:
    if x==1:
        cnt+=1 #맞았을 때 가산점
        sum+=cnt
    else:
        cnt=0 #틀렸다면 0으로 초기화
print(sum)
