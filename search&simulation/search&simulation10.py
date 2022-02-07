#스도쿠 검사

#import sys
#sys.stdin=open("input.txt", "r")

def check(a):
    for i in range(9):
        ch1=[0]*10 #행
        ch2=[0]*10 #열
        for j in range(9):
            #a에서 나온 숫자로 ch에 해당하는 인덱스에 1을 채움
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9: #둘 중 하나라도 9가 아니면(채워지지 않았다면)
            return False
        
    for i in range(3):
        for j in range(3):
            ch3=[0]*10 #3x3 그룹
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1 #그룹별로 검사
            if sum(ch3)!=9: #채워지지 않았다면
                return False
    return True

a=[list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
