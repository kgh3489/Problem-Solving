import sys

input = sys.stdin.readline

n = int(input())
staff = set() # 동명이인이 없으므로 set으로 선언

for i in range(n):
    name, state = input().split()
    if state == "enter": # 출근했다면 출근기록에 추가
        staff.add(name)
    elif state == "leave": #퇴근했다면 출근기록에서 삭제
        staff.remove(name)
        
staff = sorted(list(staff), reverse=True) # 리스트로 변환 후, 내림차순으로 정렬

for i in staff:
    print(i)
