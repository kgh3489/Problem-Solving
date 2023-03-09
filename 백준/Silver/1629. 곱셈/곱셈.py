def dac(a,b,c):
    if b == 1:
        return a % c
    
    if b % 2 == 0:
        return (dac(a,b//2,c) ** 2)%c
    else: # b가 홀수면 a를 한 번 더 곱함
        return ((dac(a,b//2,c) ** 2)*a)%c

a,b,c = map(int,input().split())
print(dac(a,b,c))