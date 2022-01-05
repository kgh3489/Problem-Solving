a=1
print(a)
a1=3
print(a, a1)
A, B, C = 3, 2, 1
print(A,B,C)

#값 교환
k, m = 10, 20
print(k, m)
k, m = m, k
print(k, m)

#변수 타입
a=12345.5
print(type(a))
a='cola'
print(type(a))

#출력방식
a,b,c=1,2,3
print(a,b,c)

print("number:        ",a,b,c)
print(a,b,c, sep=", ")
print(a,b,c, sep="\n")
print(a,b,c, end=" k\n")

#변수입력과 연산자
a=input("입력하세요: ")
print(a)
a, b = input("숫자를 입력하세요: ").split()
print(a+b) #문자로 출력
a = int(a)
b = int(b)
print(a+b) #숫자로 출력
a, b = map(int, input("숫자를 입력하세요: ").split())
print(a+b) #숫자로 출력
