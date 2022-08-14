N = int(input())
divisor = []

if N == 1:
    pass
else:
    for i in range(2, N+1):
        if N % i == 0: #N의 약수를 찾음
            divisor.append(i)
            
    for j in divisor:
        while N % j == 0: #약수로 나눠진다면
            print(j) #그 약수를 출력
            N = N // j