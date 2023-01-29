N, M = map(int, input().split())
A = list(map(int, input().split()))
res = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            max_num = 0
            max_num += A[i]+A[j]+A[k]
            if max_num <= M and max_num >= res:
                res = max_num
print(res)
