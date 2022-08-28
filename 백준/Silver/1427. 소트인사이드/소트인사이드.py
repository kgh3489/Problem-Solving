N = int(input())
num = []
for i in str(N):
    num.append(int(i)) #N을 한 자리씩 리스트에 저장
num.sort(reverse = True) #내림차순으로 정렬
for j in num:
    print(j, end = "")