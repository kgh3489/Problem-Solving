#격자판 최대합

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)] #2차원 리스트 생성
largest=-2147000000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j] #행
        sum2+=a[j][i] #열

    #최댓값이라면 저장   
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
        
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i] #대각선1
    sum2+=a[i][n-i-1] #대각선2

#최댓값이라면 저장    
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
    
print(largest)
