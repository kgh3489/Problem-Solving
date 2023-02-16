from collections import deque

N, M = map(int, input().split())
target = deque(list(map(int, input().split())))
nums = deque([i+1 for i in range(N)])
ans = 0

while target: # 다 뽑아낼 때까지 반복
    idx = -1
    for i, v in enumerate(nums):
        if v == target[0]:
            idx = i
    
    # 위에서 가져온 인덱스 번호로 회전할 방향을 결정
    if idx <= len(nums)//2:
        while target[0] != nums[0]:
            nums.rotate(-1)
            ans += 1
        target.popleft()
        nums.popleft()
    else:
        while target[0] != nums[0]:
            nums.rotate(1)
            ans += 1
        target.popleft()
        nums.popleft()
print(ans)
