#씨름 선수(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
body=[]

for _ in range(n):
    a, b=map(int, input().split())
    body.append((a,b))

body.sort(reverse=True)#키를 내림차순으로 정렬
largest=0
cnt=0

for x, y in body:
    #키가 내림차순을 정렬됐기 때문에 몸무게를 비교하여 저장된 최댓값보다 크다면 카운트
    if y>largest:
        largest=y
        cnt+=1
print(cnt)
