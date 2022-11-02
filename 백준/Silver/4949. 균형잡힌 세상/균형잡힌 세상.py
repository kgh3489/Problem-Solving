import sys

input = sys.stdin.readline

while 1:
    s = input().rstrip()
    stack = [] #한 문장을 담을 스택
    if s == ".": #점 하나면 종료
        break
    '''
    1. 여는 괄호라면 append
    2. 닫는 괄호일 때, 스택 맨 위의 문자가
    같은 여는 괄호라면 pop
    다른 여는 괄호이거나 스택이 비어있다면 균형잡힌 문자열 아님

    '''
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if not stack or stack[-1] == "[":
                print("no")
                break
            elif stack[-1] == "(":
                stack.pop()
        elif i == "]":
            if not stack or stack[-1] == "(":
                print("no")
                break
            elif stack[-1] == "[":
                stack.pop()
    else:
        #스택이 비어있다면 균형잡힌 문자열
        if stack: 
            print("no")
        else:
            print("yes")
            