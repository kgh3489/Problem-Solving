#숫자만 추출

#import sys
#sys.stdin=open("input.txt", "r")

s=input()
res=0

for x in s:
    if x.isdecimal(): #x가 int로 변환 가능하다면
        res=res*10+int(x)
print(res)

cnt=0
for i in range(1, res+1):
    if res%i==0: #i가 약수라면
        cnt+=1
print(cnt)
