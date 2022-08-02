def solution(arr):
    answer = [] #답을 담을 리스트
    for i in range(len(arr)): #arr의 길이만큼 반복
        answer.append(arr[i])
        if i >= 1: #첫 번째 인덱스부터 비교
            if answer[-2] == answer[-1]: #현재 요소가 앞의 요소와 같다면(연속됐다면)
                answer.pop() #현재 요소를 리스트에서 제거
    return answer