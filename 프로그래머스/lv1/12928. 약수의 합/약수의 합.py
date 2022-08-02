def solution(n):
    answer = 0
    for i in range(1, n+1): #i가 1~n까지 돌면서
        if n%i == 0: #n을 i로 나눈 나머지가 0이라면 (i가 n의 약수라면)
            answer += i #모두 더함
    return answer