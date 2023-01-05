N = int(input())
rings = list(map(int, input().split()))


for i in range(1, N):
    a = 0 #최대공약수 저장
    for j in range(1, min(rings[0], rings[i])+1): #최대공약수를 구함
        if rings[0] % j == 0 and rings[i] % j == 0: 
            a = j
    print(f"{rings[0]//a}/{rings[i]//a}")