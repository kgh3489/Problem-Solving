#뒤집은 소수

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

def reverse(x):
    res=0
    while x>0:
        t=x%10 #일의 자리 수를 저장
        res=res*10+t #10을 곱하고 일의 자리를 더함
        x=x//10 #x의 자릿 수를  한 자리 내리고 반복
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): #x의 절반까지 반복(그 이후엔 약수가 없음)
        if x%i==0: #x가 i로 나누어 떨어지면
            return False
    return True

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
