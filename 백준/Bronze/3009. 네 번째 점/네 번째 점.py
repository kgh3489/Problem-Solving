list_x = []
list_y = []

for _ in range(3): #세 번 반복하면서
    x, y = map(int, input().split())
    #x, y좌표를 각각 리스트에 저장
    list_x.append(x)
    list_y.append(y)
    
for i in list_x:
    if list_x.count(i) <= 1: #세 개의 좌표 중 쌍이 없는 좌표가 있다면
        print(i, end= " ") # 그 좌표를 출력
for j in list_y:
    if list_y.count(j) <= 1:
        print(j)