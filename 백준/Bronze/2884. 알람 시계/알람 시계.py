H, M = map(int, input().split())
if M-45 >= 0:
    print(H, M-45, end = " ")
else:
    if H == 0:
        H = 23
    else:
        H -= 1
    print(H, abs(M+15), end = " ")