N = int(input())
i = 0
res = 0
while i <= N:
    i += 1
    list_i = list(map(int, str(i)))
    res = sum(list_i)+i
    if res == N:
        print(i)
        break
    if i == N:
        print(0)