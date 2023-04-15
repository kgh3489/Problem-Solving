def solution(s):
    answer = [0, 0] # 이진 변환 횟수, 제거한 0의 개수
    
    while s != "1":
        cnt = 0 # 문자열에서 0의 개수
        answer[0] += 1
        for i in s:
            if i == "1":
                cnt += 1
            else:
                answer[1] += 1
        s = format(cnt, 'b') # 이진수 변환

    return answer

