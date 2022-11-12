A = []
for i in range(9):
    N = int(input())
    A.append(N)
print(max(A))
print(A.index(max(A))+1)