N, K = map(int, input().split())
coins = []

for _ in range(N):
    coin = int(input())
    if coin <= K: # 가치보다 큰 동전은 사용하지 않음
        coins.append(coin)
coins.sort(reverse=True) # 내림차순으로 정렬

cnt = 0 # 동전 개수
i = 0 # 사용할 동전
while K > 0:
    if K >= coins[i]:
        cnt += K // coins[i]
        K = K % coins[i]
    else:
        i += 1
print(cnt)
