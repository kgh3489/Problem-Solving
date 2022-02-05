#곶감(모래시계)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
m=int(input())

for i in range(m):
    h, t, k=map(int, input().split()) #행번호, 방향, 회전하는 격자 수
    if t==0: #왼쪽으로 회전할 때
        for _ in range(k): #k만큼 회전
            a[h-1].append(a[h-1].pop(0)) #첫번째 인덱스 제거 후 맨 뒤에 추가
    else: #오른쪽으로 회전할 때
        for _ in range(k): #k만큼 회전
            a[h-1].insert(0, a[h-1].pop()) #마지막 인덱스 제거 후 맨 앞에 추가

res=0
s=0
e=n-1

for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2: #중간에 오기 전까지
        s+=1
        e-=1
    else: #중간 이후
        s-=1
        e+=1
print(res)
