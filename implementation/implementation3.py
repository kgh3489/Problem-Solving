#K번째 큰 수 구하기

#import sys
#sys.stdin=open("input.txt", "rt")

n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set() #set 자료구조로 변경(중복을 제거함)
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m]) #append 대신 add
res=list(res) # 정렬을 위해 set -> list로 변경
res.sort(reverse=True) #내림차순으로 정렬
print(res[k-1])
