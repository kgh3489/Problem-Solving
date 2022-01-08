#리스트와 내장함수

import random as r

#빈 리스트 만드는 법 
a=[]
b=list()

a=[1, 2, 3, 4, 5]
print("리스트 a:", a)
print(a[0])

b=list(range(1, 11))
print("리스트 b:", b)

c=a+b
print(c)

a.append(6) #리스트 맨 뒤에 값 추가
a.insert(3, 7) #특정 위치에 값 추가 (3번 인덱스에, 값 7 추가)
a.pop() #맨 뒤에 값 제거
a.pop(3) #3번 인덱스 값 제거
a.remove(4) #4를 찾아서 제거
a.index(5) #5를 찾아서 인덱스 번호 반환

print(sum(a))
print(max(a))
print(min(a))

r.shuffle(a) #무작위로 값을 섞음
print(a)
a.sort() #오름차순 정렬
print(a)
a.sort(reverse=True) #내림차순 정렬
print(a)

a.clear()
a=[23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))

for i in range(len(a)):
    print(a[i])

for x in a:
    print(x)

for x in a:
    if x%2==1:
        print(x)

for x in enumerate(a): #인덱스 번호와 그에 해당하는 값을 튜플 형태로 반환
    print(x)
#$%$리스트는 값을 변경할 수 있지만 튜플은 변경 불가능$%$

for x in enumerate(a): #튜플을 원소값으로 찍어줌
    print(x[0], x[1])

for index, value in enumerate(a): #enumerate 일반적인 표현 형태
    print(index, value)

if all(60>x for x in a): #모든 조건이 60>x이면 True 반환
    print("모두 60보다 작습니다!")
else:
    print("ㅠㅠㅠ")

if any(15>x for x in a): #한 번이라도  15>x이면 True 반환
    print("15보다 큰 값이 있네요!")
else:
    print("ㅠㅠㅠ")

#2차원 리스트

a=[0]*10

a=[[0]*3 for _ in range(3)] #가로로 출력
print(a)

for x in a: #2차원 형태로 출력
    print(x)

for x in a: #원소 형태로 출력
    for y in x:
        print(y, end=' ')
    print()