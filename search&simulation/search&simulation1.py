#회문 문자열 검사

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())

for i in range(n):
    s=input()
    s=s.upper() #대소문자를 구분하지 않기 때문에 모두 대문자로 바꿔줌
    
    if s==s[::-1]: #원래 문자와 뒤집은 문자가 같다면
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))

'''

n=int(input())

for i in range(n):
    s=input()
    s=s.upper()
    size=len(s)

    for j in range(size):
        if s[j]!=s[-1-j]: #같은 위치의 인덱스를 비교
            print("#%d NO" %(i+1))
            break
        else:
            print("#%d YES" %(i+1))
'''
