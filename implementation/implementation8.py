#소수(에라토스테네스 체)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
ch=[0]*(n+1) #소수인지 판별할 리스트 생성
cnt=0 #소수의 개수를 저장

for i in range(2, n+1):
    if ch[i]==0: #소수라면
        cnt+=1
        for j in range(i, n+1, i): #나온 소수의 배수들은
            ch[j]=1 #소수가 아님
print(cnt)
