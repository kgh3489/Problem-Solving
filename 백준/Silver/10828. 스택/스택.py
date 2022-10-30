import sys
input = sys.stdin.readline

n = int(input())
stack = []

for i in range(n):
    order = input().rstrip()
    if order == "pop":
        if len(stack) == 0:
            print(-1)
            continue
        stack_pop = stack.pop()
        print(stack_pop)
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
            continue
        print(stack[-1])
    else:
        stack_push = int(order[5:])
        stack.append(stack_push)