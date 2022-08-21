def solution(n, m):
    answer = []
    a = []  #약수를 저장할 리스트

    for i in range(1, max(n, m)+1):
        if n%i == 0 and m%i == 0: #둘 모두 나누어 떨어지면 약수
            a.append(i)
    answer.append(max(a)) #가장 큰 값이 최대공약수
    
    for j in range(max(n, m), n*m+1): #둘 중 큰 값부터 둘을 곱한 값까지 반복
        if j%n == 0 and j%m == 0: #그 수가 둘로 모두 나누어 떨어진다면
            answer.append(j)
            break
    return answer
