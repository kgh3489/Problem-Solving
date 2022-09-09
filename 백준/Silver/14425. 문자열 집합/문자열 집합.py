import sys

N, M = map(int, sys.stdin.readline().split())
S = []
cnt = 0

for _ in range(N):
    word = sys.stdin.readline()
    S.append(word)

for i in range(M):
    check_word = sys.stdin.readline()
    if check_word in S:
        cnt += 1
print(cnt)