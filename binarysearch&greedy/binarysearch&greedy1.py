#이분검색

#import sys
#sys.stdin=open("input.txt", "r")

n, m=map(int, input().split())
a=list(map(int, input().split()))
a.sort()
lt=0 #처음
rt=n-1 #마지막

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m: #원하는 값을 찾았다면
        print(mid+1)
        break
    elif a[mid]>m: #원하는 값보다 크다면
        rt=mid-1 #rt를 이동
    else: #원하는 값보다 작다면
        lt=mid+1 #lt를 이동
