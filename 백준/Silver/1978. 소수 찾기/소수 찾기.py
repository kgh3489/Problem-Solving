N = int(input())
a = list(map(int, input().split()))
cnt = 0

for i in range(N):
    if a[i] == 1: #1은 소수가 아님
        cnt += 0
    else:
        if a[i] % 2 == 0: #짝수일 때
            if a[i] == 2: #2는 소수
                cnt += 1
            else: #2를 제외한 나머지는 소수가 아님
                continue
        else: #1을 제외한 홀수일 때
            for j in range(2, a[i]+1): #주어진 수까지 반복하면서
                if j < a[i]:
                    if a[i] % j == 0: #약수가 나온다면 소수가 아님
                        break
                    else:
                        continue
                else: 
                    cnt += 1 #주어진 수까지 왔다면 소
print(cnt)