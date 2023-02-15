import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
res = deque()

for i in range(N):
    command = input().split()
    command[-1].rstrip()
    
    if command[0] == "push_front":
        res.appendleft(command[1])
    elif command[0] == "push_back":
        res.append(command[1])
    elif command[0] == "pop_front":
        if not res: # 비어있으면 -1
            print(-1)
        else:
            print(res.popleft())
    elif command[0] == "pop_back":
        if not res: # 비어있으면 -1
            print(-1)
        else:
            print(res.pop())
    elif command[0] == "size":
        print(len(res))
    elif command[0] == "empty":
        if not res: # 비어있으면 1
            print(1)
        else:
            print(0)
    elif command[0] == "front":
        if not res: # 비어있으면 -1
            print(-1)
        else:
            print(res[0])
    elif command[0] == "back":
        if not res: # 비어있으면 -1
            print(-1)
        else:
            print(res[-1])
