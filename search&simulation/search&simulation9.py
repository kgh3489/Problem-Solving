#봉우리

#import sys
#sys.stdin=open("input.txt", "r")

#상하좌우 탐색
dx=[-1, 0, 1, 0]
dy=[0, 1, 0 ,-1]

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

#가장자리 0으로 초기화
a.insert(0, [0]*n)
a.append([0]*n)
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt=0
for i in range(1, n+1): #0번이 아닌 1번부터 반복
    for j in range(1, n+1):
        if all(a[i][j]>a[i+dx[k]]+[j+dy[k]] for k in range(4)) #상하좌우보다 크다면
            cnt+=1
print(cnt)
