X = int(input())
N = int(input())
cnt = 0

for _ in range(N):
    a, b = map(int, input().split())
    cnt += a * b #가격*개수를 cnt에 더함
if cnt == X :
    print("Yes")
else:
    print("No")