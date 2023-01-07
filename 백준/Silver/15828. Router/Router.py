import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
router = deque() # 먼저 들어온 것을 빼내기 위해 덱으로 deque로 선언

while True:
    packet = int(input())
    if packet == 0:
        router.popleft() # 패킷 하나를 처리
    elif packet == -1:
        break # -1이면 입력이 끝남
    elif N != 0 and len(router) < N:
        router.append(packet) # 패킷 입력

print(*router if len(router) != 0 else "empty")
