#p와 y의 개수를 비교
#같으면 True, 다르면 False, 하나도 없으면 True
def solution(s):
    return s.lower().count("p") == s.lower().count("y")
#문자열 s를 모두 소문자로 바꾸고 p와 y의 개수를 비교
#같으면 True, 다르면 False를 return 
