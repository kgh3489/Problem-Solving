#최솟값 구하기

arr=[5, 3, 7, 9, 2, 5, 2, 6]
arrMin=float('inf') #무한대 값을 넣어서 첫 번째 인덱스와 비교 시 그 값을 저장
for i in range(len(arr)): #0번 인덱스부터 비교
    if arr[i]<arrMin:
        arrMin=arr[i]
print(arrMin)
