import sys

N = int(sys.stdin.readline())
coordinate = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append((x, y))
coordinate.sort(key=lambda k: (k[1], k[0])) #람다식을 활용하여 y로 먼저 정렬 후 같다면 x로 정렬

for i in range(len(coordinate)):
    print(coordinate[i][0], coordinate[i][1])