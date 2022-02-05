#사과나무(다이아몬드)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res=0
s=e=n//2 #리스트의 가운데

for i in range(n):
    for j in range(s, e+1): #다이아몬드의 범위
        res+=a[i][j] 
    if i<n//2: #중간에 도달할 때까지 범위 증가
        s-=1
        e+=1
    else: #도달한 후 범위 감소
        s+=1
        e-=1
print(res)
        
