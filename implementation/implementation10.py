#주사위 게임

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
res=0
max=0

for i in range(n):
    tmp=input().split()
    tmp.sort() #가장 큰 눈을 찾기위해 정렬
    a, b, c=map(int, tmp) #a, b, c로 입력된 수 매핑

    if a==b and b==c: #전부 같다면
        money=10000+a*1000
    elif a==b or a==c: #둘만 같다면1
        money=1000+a*100
    elif b==c: #둘만 같다면2
        money=1000+b*100
    else: #모두 다르다면
        money=c*100

    if money>res: #최댓값 판별
        res=money
print(res)
