#카드 역배치

#import sys
#sys.stdin=open("input.txt", "r")

a=list(range(21)) #0-20까지의 리스트 생성

for _ in range(10): #10번 반복
    s, e=map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i] #해당 위치의 카드 바꿈

a.pop(0) #0번 인덱스 제거

for x in a:
    print(x, end=' ')
