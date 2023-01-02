def dfs():
    if len(s) == M:
        print(*s) #unpacking
        return

    for i in range(1, N+1):
        if i in s:
            continue

        s.append(i)
        dfs()  # 함수 다시 호출
        s.pop()  # 원상복귀


        
N, M = map(int, input().split())
s = []
dfs()

