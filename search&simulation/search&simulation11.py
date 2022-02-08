#격자판 회문수

#import sys
#sys.stdin=open("input.txt", "r")

board=[list(map(int, input().split())) for _ in range(7)]
cnt=0

for i in range(3): #연속된 5개의 숫자를 확인할 것이기 때문에 3번만 반복하면 됨
    for j in range(7):
        tmp=board[j][i:i+5] #1번째~5번째 숫자
        if tmp==tmp[::-1]: #행 검사
            cnt+=1
        for k in range(2): #길이가 5이므로 5//2
            if board[i+k][j]!=board[i+5-k-1][j]: #열 검사
                break;
        else:
            cnt+=1
        
print(cnt)



'''
<회문의 길이가 가변적일 때 코드>
import sys
sys.stdin=open("input.txt", "r")
board=[list(map(int, input().split())) for _ in range(7)]
cnt=0
len=5
for i in range(3):
    for j in range(7):
        tmp=board[j][i:i+len]
        if tmp==tmp[::-1]:
            cnt+=1
        #tmp=board[i:i+5][j] 앞 행은 리스트가 아니라서 슬라이스가 안된다.
        for k in range(len//2):
            if board[i+k][j]!=board[len-k+i-1][j]:
                break;
        else:
            cnt+=1
        
print(cnt)
'''
