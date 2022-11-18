A = []
for i in range(10):
    K = int(input())%42
    A.append(K)
set_A = set(A)
print(len(set_A))