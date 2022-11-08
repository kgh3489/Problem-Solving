n = int(input())

fibonacci = [0, 1] #F(0), F(1)
for i in range(2, n+1): #n>=2일 때부터 식이 성립하기 때문에 2부터 반복
    num = fibonacci[i-1] + fibonacci[i-2] #F(n) = F(n-1) + F(n-2)
    fibonacci.append(num)
print(fibonacci[n])