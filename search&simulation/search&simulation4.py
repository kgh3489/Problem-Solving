#두 리스트 합치기

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))
m=int(input())
b=list(map(int, input().split()))

'''
k=a+b
k.sort()
for i in range(len(k)):
    print(k[i], end=" ")
    
#sort를 사용하여 속도가 느림
'''

p1=p2=0
c=[]

while p1<n and p2<m: #두 조건 모두 만족할 때까지만 반복
    if a[p1]<=b[p2]: #a의 요소가 더 작다면
        c.append(a[p1]) #a를 붙인다
        p1+=1
    else: #b의 요소가 더 작다면
        c.append(b[p2]) #b를 붙인다
        p2+=1
if p1<n: #while문 종료 시 p1이 남아있다면
    c=c+a[p1:]
if p2<m: #while문 종료 시 p2가 남아있다면
    c=c+b[p2:]

for x in c:
    print(x, end=' ')
