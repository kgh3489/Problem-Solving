#반복문 문제 풀이
n=int(input())
for i in range(1, n+1):
    print(i)

#1부터 n까지 홀수 출력
n=int(input())
for i in range(1, n+1):
    if i%2==1:
        print(i)

#1부터 n까지 합
n=int(input())
sum=0
for i in range(1, n+1):
    sum=sum+i
    print(sum)

#n의 약수 출력
n=int(input())
for i in range(1, n+1):
    if n%i==0:
        print(i, end='..')


#중첩 반복문
for i in range(5):
    for j in range(5):
        print(i, j)

#별 하나씩 늘려가며 출력
for i in range(5):
    for j in range(i+1):
        print("*", end=' ')
    print()

#별 하나씩 줄여가며 출력
for i in range(5):
    for j in range(5-i):
        print("*", end=' ')
    print()


