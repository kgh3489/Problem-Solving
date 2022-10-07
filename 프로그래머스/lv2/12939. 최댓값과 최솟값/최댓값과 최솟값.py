def solution(s):
    list_s = list(map(int, s.split())) #문자열 s를 공백으로 나눠 리스트에 저장
    answer = f"{str(min(list_s))} {str(max(list_s))}" #최솟값과 최댓값을 다시 문자열로 저장
    
    return answer