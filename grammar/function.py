#함수

def add(a, b):
    c=a+b
    return c

x=add(3, 2)
print(x)

def add2(a, b):
    c=a+b
    d=a-b
    e=a*b
    return c, d, e
print(add2(3, 2)) #리턴값이 2개 이상인 경우 튜플로 반환

def isPrime(x): #x가 소수인지 판별하는 함수
    for i in range(2, x):
        if x%i==0:
            return False
    return True
    
a=[12, 13, 7, 9, 19]
for k in a:
    if isPrime(k):
        print(k, end=' ') #리턴값이 True일 때 k 출력
print()


#람다함수
#lambda 매개변수 : 표현식

def plus_one(x):
    return x+1
print(plus_one(1))

"""위아래가 같은 의미"""

plus_one2=lambda x: x+1
print(plus_one2(1))

a=[1, 2, 3]

print(list(map(plus_one, a)))

"""위아래가 같은 의미"""

print(list(map(lambda x: x+1, a)))


