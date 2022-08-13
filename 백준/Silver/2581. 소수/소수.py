import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime = []

for i in range(M, N+1):
    for j in range(2, i+1):
        if j == i: #i가 소수라면
            prime.append(i)
        if i % j == 0: #i가 소수가 아니라면 다음 숫자로 넘어감
            break
            
if len(prime) == 0: #소수가 없다면
    print(-1)
else: 
    print(sum(prime))
    print(prime[0])