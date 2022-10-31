import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    num = int(input())
    if num == 0:
        stack.pop() #0이라면 최근의 수를 꺼냄
    else:
        stack.append(num) #0이 아니면 그 수를 추가


if len(stack) == 0:
    print(0) #리스트가 비었을 경우 0을 출력
else:
    print(sum(stack))