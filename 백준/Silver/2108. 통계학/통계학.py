import sys
from collections import Counter #collections 모듈의 Counter 클래스 사용

N = int(sys.stdin.readline())
num = []
for _ in range(N):
    num.append(int(sys.stdin.readline())) 

#산술평균
print(round(sum(num)/N))

#중앙값
num.sort()
print(num[N//2])

#최빈값
counter_num = Counter(num).most_common() #리스트 num을 Counter로 딕셔너리로 만든 후, 최빈값을 찾음 
if len(num) > 1: #리스트 길이가 1이 넘는다면 최빈값이 2개 이상인지 확인
    if counter_num[0][1] == counter_num[1][1]: #2개 이상이라면
        print(counter_num[1][0]) #2번째 수 출력
    else:
        print(counter_num[0][0])
else:
    print(counter_num[0][0])

#범위
print(max(num) - min(num))