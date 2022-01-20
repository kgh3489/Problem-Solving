#대푯값 구하기

#import sys
#sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

ave=sum(a)/n #리스트의 평균 값

#반올림 
ave=ave+0.5
ave=int(ave)

min=2147000000 #정수형에서 가장 큰 값

for idx, x in enumerate(a): #리스트 a를 돌 때
    tmp=abs(x-ave) #요소에서 평균을 뺀 절댓값
    if tmp<min: #절댓값이 최솟값보다 작다면
        min=tmp #그 값을 min에 저장
        score=x 
        res=idx+1
    elif tmp==min: #최솟값과 절댓값이 같을 때
        if x>score: #저장된 score보다 x가 더 크다면
            score=x #그 값을 score에 저장
            res=idx+1
print(ave, res)
