# 가장 시간이 적은 순서대로 더해야 함

N = int(input())
atm = list(map(int, input().split()))
atm.sort() # 오름차순 정렬

total = 0
for i in range(N):
    total += sum(atm[:i+1]) # 첫 번째 사람 ~ i 번쨰 사람
print(total)

