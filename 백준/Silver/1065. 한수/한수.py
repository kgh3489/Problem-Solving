N = int(input())
cnt = 0 #한수의 개수
for i in range(1, N+1):
    if i < 100: #100보다 작은 수는 모두 한수
        cnt += 1
    else:
        list_i = list(map(int, str(i)))
        #(십의 자리수-일의 자리수)와 (백의 자리수-십의 자리수)가 같다면
        if (list_i[1]-list_i[0]) == (list_i[2]-list_i[1]):
            cnt += 1
print(cnt)