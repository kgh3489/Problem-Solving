nums1 = list(map(str, input().split("-"))) # - 되는 수가 제일 크도록 분리

ans = 0
for i in range(len(nums1)):
    nums2 = map(int, nums1[i].split("+")) # 분리된 수들을 int형으로 변환
    # 첫 번째 수만 더하고 나머지는 모두 뻄
    if i == 0:
        ans += sum(nums2) 
    else:
        ans -= sum(nums2)
print(ans)
