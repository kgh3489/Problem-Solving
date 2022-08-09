chess = [1, 1, 2, 2, 2, 8]
white_piece = list(map(int, input().split()))
for i in range(6):
    print(chess[i]-white_piece[i], end = " ") #각 말마다 몇 개를 더하거나 빼야되는지 구함