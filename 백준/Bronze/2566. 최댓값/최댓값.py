nums = []
for _ in range(9):
    nums.append(list(map(int, input().split())))

max_num, row, col = -1, -1, -1 #최댓값, 행, 열

for i in range(len(nums)):
    for j in range(len(nums[i])):
        if nums[i][j] > max_num:
            max_num = nums[i][j]
            row = i
            col = j
            
print(max_num)
print(row+1, col+1)
