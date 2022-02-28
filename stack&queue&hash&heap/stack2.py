#쇠막대기(스택)

#import sys
#sys.stdin=open("input.txt", "r")

s=input()
stack=[]
cnt=0
        
for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i]) #막대기를 쌓음
    else:
        stack.pop() #레이저이거나 막대기의 끝이므로 pop
        if s[i-1]=='(': #레이저라면
            cnt+=len(stack)
        else: #막대기의 끝이라면
            cnt+=1
        
print(cnt)
