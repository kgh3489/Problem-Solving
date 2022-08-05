x, y, w, h  = map(int, input().split())
print(min(x, y, w-x, h-y)) #4가지 방향의 직선거리 중 최솟값을 출력