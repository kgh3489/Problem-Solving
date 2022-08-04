import sys

N = int(sys.stdin.readline())
res = [0] * 10001
for i in range(N):
    res[int(sys.stdin.readline())]+=1 #리스트에 해당하는 숫자를 인덱스로 받아 저장

for i in range(10001):
    if res[i] != 0: #요소가 비어있지 않다면
        for _ in range(res[i]): #더해진 숫자만큼 해당 인덱스를 출력
            print(i)