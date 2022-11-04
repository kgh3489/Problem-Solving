N = int(input())
res = 1
room = 1
if N == 1:
    print(1)
else:
    while 1:
        res+=1
        room+=6*(res-1)
        if N<=room:
            print(res)
            break