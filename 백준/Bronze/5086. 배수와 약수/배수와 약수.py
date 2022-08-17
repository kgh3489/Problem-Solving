while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0: #둘 다 0이면 종료
        break
    if b%a == 0: #a가 b의 약수라면
        print("factor")
    elif a%b == 0: #a가 b의 배수라
        print("multiple")
    else:
        print("neither")