N = int(input())
res = 1
for i in range(1, N+1): #0보다 크거나 같으므로 1부터 반복
    res *= i #i를 1씩 증가시키면서 순차적으로 곱함
print(res)