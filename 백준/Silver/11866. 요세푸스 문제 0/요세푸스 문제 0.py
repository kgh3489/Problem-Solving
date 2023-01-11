from collections import deque

N, K = map(int, input().split())

arr = deque([i + 1 for i in range(N)]) # N명의 리스트를 deque로 선언
josephus = [] # 결과 순열
while len(josephus) != N: #결과 순열의 길이가 N이 될 때까지 반복
    arr.rotate(-(K-1)) #deque를 K-1만큼 왼쪽으로 회전
    num = arr.popleft()
    josephus.append(num)

# 출력
print("<", end="")
for i in josephus:
    if i == josephus[-1]:
        print(i, end="")
    else:
        print(i, end=", ")    
print(">")
