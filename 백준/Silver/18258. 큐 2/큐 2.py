import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([]) #pop(n)이 O(n)의 시간복잡도를 요구하기 때문에 deque로 지정
for _ in range(n):
    order = input().rstrip()
    if order == "pop":
        if queue:
            print(queue[0])
            queue.popleft() #제일 왼쪽 pop
        else:
            print(-1)
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif order == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif order == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(order[5:])
