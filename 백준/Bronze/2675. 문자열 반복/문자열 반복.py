T = int(input())
for i in range(T):
    R, S = map(str, input().split())
    R = int(R)
    S = list(S)
    for j in S:
        print(j*R, end="")
    print(sep="\n")
