N = int(input())
res = N
cnt = 0
while 1:
    A = res//10
    B = res%10
    res = 10*B+(A+B)%10
    cnt+=1
    if res == N:
        break
print(cnt)