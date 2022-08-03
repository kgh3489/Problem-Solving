def solution(x, n):
    plus = x #증가시킬 수
    answer = []
    for _ in range(n): #n만큼 반복하며
        answer.append(x) #나온 수를 리스트에 append
        x += plus #수를 plus만큼 증가
    return answer