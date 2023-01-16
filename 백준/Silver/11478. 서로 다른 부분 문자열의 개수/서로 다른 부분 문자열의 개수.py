S = input()
total = set()

for i in range(len(S)):
    for j in range(i,len(S)):
        total.add(S[i:j+1]) # i번째 문자부터 부분문자열 구하기
print(len(total))
