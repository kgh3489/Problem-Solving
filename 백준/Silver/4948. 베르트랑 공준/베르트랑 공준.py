import math

m = 123456

array1 = [True for _ in range(2 * m + 1)] #소수 판별을 위한 리스트설정(True면 소수)
array1[0], array1[1] = False, False


for i in range(2, int(math.sqrt(2 * m) + 1)):
    if array1[i]: #만약 array1[i]가 True(소수)라면
        j = 2 #i에 곱해줄 j값을 2부터 설정
        while i * j <= 2 * m: #i * j 가 2* 123456 보다 작거나 같다면
            array1[i * j] = False #해당 i*j의 값은 소수가 아니므로 False로 설정
            j += 1 #j를 1씩 증가

while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range(n+1, 2 * n + 1): #n+1(n보다 커야하기 때문) 부터 2 * n + 1 까지 설정
        if array1[i]:  #만약 해당 i가 True(소수) 라면
            count += 1 #count값에다 +1
    print(count)  #count 값 출력