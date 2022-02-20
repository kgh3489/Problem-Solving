#창고 정리(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

l=int(input())
a=list(map(int, input().split()))
m=int(input())
a.sort()

for _ in range(m):
    #제일 작은 인덱스(a[0])은 1 감소, 제일 큰 인덱스(a[l-1])은 1 증가
    a[0]+=1
    a[l-1]-=1
    a.sort()

print(a[l-1]-a[0])

'''
제일 높은 곳에서 제일 낮은 곳으로 1이 이동
제일 높은 곳, 제일 낮은 곳 찾기 => sort하면 쉬움
'''
