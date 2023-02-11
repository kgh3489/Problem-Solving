N = int(input())
list_x = [] #몸무게를 담을 리스트
list_y = [] #키를 담을 리스트
for _ in range(N): #몸무게와 키를 각각 리스트에 담음
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

for i in range(N):
    rank = 1 #나보다 덩치가 큰 사람이 아무도 없다면 1위
    for j in range(N):
        if list_x[i] < list_x[j] and list_y[i] < list_y[j]: #나보다 덩치가 크다면 
            rank += 1 #순위 하락
    print(rank, end = " ")