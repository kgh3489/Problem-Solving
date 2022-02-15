#회의실 배정(그리디)

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
meeting=[]

for _ in range(n):
    a, b=map(int, input().split())
    meeting.append((a, b)) #튜플 형태로 리스트에 추가
meeting.sort(key=lambda x : (x[1], x[0])) #끝나는 시간을 선순위로 정렬

et=0
cnt=0

for x,y in meeting:
    if x>=et: #시작 시간이 끝나는 시간 후라면
        et=y 
        cnt+=1

print(cnt)
