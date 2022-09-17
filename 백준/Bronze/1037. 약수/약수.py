cnt = int(input())
real_divisor= list(map(int, input().split()))

print(max(real_divisor) * min(real_divisor)) #약수 중 가장 큰 수 X 가장 작은 수
