#자릿수의 합

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))
 
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10 #10으로 나눈 나머지를 sum에 저장
        x=x//10 #x는 10으로 나눈 몫을 저장
    return sum

max=-2147000000
for x in a:
    tot=digit_sum(x) #tot에 자릿수의 합 저장
    if tot>max: #tot이 가장 큰 수라면
        max=tot 
        res=x #인덱스에 해당하는 수 저장
print(res)
