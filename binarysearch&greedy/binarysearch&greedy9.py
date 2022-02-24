#증가수열 만들기(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))
lt=0 #왼쪽에서 시작
rt=n-1 #오른쪽에서 시작
last=0 #수열의 마지막 수
res="" 
tmp=[]

while lt<=rt:
        if a[lt]>last:
           tmp.append((a[lt], 'L'))
        if a[rt]>last:
            tmp.append((a[rt], 'R'))
        tmp.sort() #append한 숫자들을 정렬
        
        if len(tmp)==0: #append 할 숫자가 없다면
            break
        else:
            res=res+tmp[0][1] #문자열 이어붙임
            last=tmp[0][0]
            if tmp[0][1]=='L':
                lt=lt+1
            else:
                rt=rt-1
            tmp.clear()

print(len(res))
print(res)
