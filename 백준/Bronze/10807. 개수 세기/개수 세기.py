N = int(input())
num = list(map(int, input().split()))
v = int(input())

cnt = 0
for i in num:
    if i == v:
        cnt += 1
print(cnt)
    