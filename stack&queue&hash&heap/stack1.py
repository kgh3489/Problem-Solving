#가장 큰 수(스택)

#import sys
#sys.stdin=open("input.txt", "r")

num, m=map(int, input().split())
num=list(map(int, str(num)))
stack=[]

for x in num:
    while stack and m>0 and stack[-1]<x: #스택이 비어있지 않고 m이 남아있고 맨 끝의 수가 마지막에 들어온 수보다 작다면
        stack.pop()
        m-=1
    stack.append(x)
    print(stack)

if m!=0: #m이 남아있다면
    stack=stack[:-m] #끝에서부터 제거

res=''.join(map(str, stack)) #리스트를 join함수로 합
print(res)
