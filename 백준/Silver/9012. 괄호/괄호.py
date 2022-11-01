import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    stack = []
    ps = input()
    for i in ps:
        if i == "(":
            stack.append(i)
        if i == ")":
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    #for문이 모두 수행된 후 스택에 "("가 있는지 검사
    else:
        if not stack:
            print("YES")
        else:
            print("NO")
