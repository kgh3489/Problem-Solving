N = int(input())
A = list(map(int, input().split()))
M = max(A)
for i in range(len(A)):
    A[i] = A[i]/M*100  
print(sum(A)/N)
