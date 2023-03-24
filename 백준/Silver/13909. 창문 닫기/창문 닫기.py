N = int(input())
cnt = 0

for i in range(1, N+1):   
    if i*i <= N:
        cnt += 1
    else:
        break
print(cnt)
