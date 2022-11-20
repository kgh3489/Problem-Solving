N = int(input())
for _ in range(N):
    res = 0
    cnt = 0
    A = list(input())
    for i in A:
        if i == 'O':
            cnt+=1
            res+=cnt
        else:
            cnt = 0
    print(res)