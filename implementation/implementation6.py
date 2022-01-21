#정다면체

#import sys
#sys.stdin=open("input.txt", "r")

n, m=map(int, input().split())
cnt=[0]*(n+m+1) #합의 개수를 넣을 리스트 cnt 생성(초기값은 모두 0)
max=-2147000000

for i in range(1, n+1):
    for j in range(1, m+1):
       cnt[i+j]+=1 #인덱스 번호에 해당하는 수가 나올 때마다 +1

for i in range(n+m+1):
    if cnt[i]>max: #가장 빈도가 높은 인덱스 확인
        max=cnt[i] #그 값을 max에 저장

for i in range(n+m+1):
    if cnt[i]==max: #max와 같은 수라면(가장 확률이 높다면)
        print(i, end=' ') #해당 요소 모두 출력
