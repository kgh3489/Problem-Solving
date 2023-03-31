N = int(input())
gomgom = set()
cnt = 0

for i in range(N):
    user = input()
    if user == "ENTER": # 새로운 사람 입장
        cnt += len(gomgom)
        gomgom.clear() # set의 모든 요소 제거
    else:
        gomgom.add(user)
cnt += len(gomgom)
print(cnt)
