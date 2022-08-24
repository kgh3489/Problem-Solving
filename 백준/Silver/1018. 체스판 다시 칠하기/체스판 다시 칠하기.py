N, M = map(int, input().split())
board = [] #잘라낼 보드
count = [] #8*8 체스판

for _ in range(N): 
    board.append(input())

for a in range(N-7): 
    for b in range(M-7):
        index1 = 0 #white로 시작인 경우
        index2 = 0 #black으로 시작인 경우
        #8*8이기 때문에 시작점부터 8번만 반복
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: #짝수인 경우 시작과 같아야함
                    if board[i][j] != 'W': 
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1
                else: #홀수인 경우 시작과 같아야함
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count)) #최솟값 출력