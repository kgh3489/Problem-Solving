grade = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0.0}

avg = 0 # (학점 × 과목평점)의 합
cnt = 0 # 학점의 총합
for i in range(20):
    majors = list(map(str, input().split()))
    majors[2].rstrip()
    
    if majors[2] == "P": # P면 계산에서 제외
        continue
    
    majors[1] = float(majors[1])
    avg += grade[majors[2]]*majors[1]
    cnt += majors[1]
print(avg/cnt)
