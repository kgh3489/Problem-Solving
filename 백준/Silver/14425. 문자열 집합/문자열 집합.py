import sys

N, M = map(int, sys.stdin.readline().split())
S = set() #set의 탐색  평균 시간복잡도는 O(1)
cnt = 0

for _ in range(N):
    word = sys.stdin.readline()
    S.add(word)

for i in range(M):
    check_word = sys.stdin.readline()
    if check_word in S:
        cnt += 1
print(cnt)