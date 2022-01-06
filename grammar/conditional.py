#조건문
x = 15
if x >= 10:
    print("검증...")
    if x%2 == 1:
        print("10이상의 홀수")

y = 7
if y>0 and y<10:
    print("y는 0보다 크고 10보다 작다")

y = 7
if 0<y<10:
    print("y는 0보다 크고 10보다 작다")

#분기문
z = -10
if z>0:
    print("양수")
else:
    print("음수")

x = 93
if x>=90:
    print('A')
elif x>=80:
    print('B')
elif x>=70:
    print('C')
elif x>=60:
    print('D')
else:
    print('F')
