C = int(input())
for _ in range(C):
    cnt = 0
    res = 0
    A = list(map(int, input().split()))
    avg = sum(A[1:])/A[0]
    for i in A[1:]:
        if i>avg:
            cnt+=1
    res = cnt/A[0]*100
    print(f'{res:.3f}%')