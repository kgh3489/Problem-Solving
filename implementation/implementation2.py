#K번째 수 구하기

#import sys
#sys.stdin=open("input.txt", "rt")

T=int(input()) #테스트 케이스 개수 입력

for t in range(T): #T만큼 반복
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split())) #자료를 리스트 형태로 입력 받음
    a=a[s-1:e] #범위만큼 슬라이싱
    a.sort() #오름차순 정렬
    print("#%d %d" %(t+1, a[k-1])) #형식대로 출력
