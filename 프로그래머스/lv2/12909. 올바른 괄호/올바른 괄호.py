def solution(s):
    stack = []
    answer = True
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer = False
                break
    
    if stack:
        answer = False
    else:
        pass

    return answer