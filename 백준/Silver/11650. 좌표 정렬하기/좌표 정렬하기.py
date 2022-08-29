import sys

N = int(input())
num = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    num.append((x, y)) #x, y좌표를 튜플 형태로 append
num.sort() #오름차순으로 정렬

for i in range(len(num)):
    print(num[i][0], num[i][1])