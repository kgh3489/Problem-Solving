#K번째 약수 구하기

#import sys
#sys.stdin=open("input.txt", "rt")

n, k=map(int, input().split()) #두 개 숫자를 한 줄로 읽어옴
cnt=0

for i in range(1, n+1): #n까지 반복
    if n%i==0: #n의 약수 구하기
        cnt+=1
    if cnt==k: #k번째 약수가 발견됐다면
        print(i) 
        break
else: #k를 발견하지 못 했다면
    print(-1)
