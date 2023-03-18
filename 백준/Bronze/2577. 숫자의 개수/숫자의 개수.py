A = int(input())
B = int(input())
C = int(input())
K = list(map(int, str(A*B*C)))
for i in range(10):
    print(K.count(i))