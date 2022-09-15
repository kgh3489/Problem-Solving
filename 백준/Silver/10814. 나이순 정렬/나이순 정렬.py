import sys

N = int(sys.stdin.readline())
users = []

for i in range(N):
    age, name = map(str, sys.stdin.readline().split())
    users.append((int(age), i, name)) #나이, 인덱스, 이름을 리스트에 저장
users.sort(key = lambda x : (x[0], x[1])) #나이로 먼저 정렬 후 인덱스 순서로 정렬

for j in users:
    print(j[0], j[2]) #나이와 이름을 출력