#회문 문자열 검사

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
for i in range(n):
    str=input()
    str=str.upper()
    if str==str[::-1]:
        print("#%d YES" %i)
    else:
        print("#%d NO" %i)
