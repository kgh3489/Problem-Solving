import sys

N = int(sys.stdin.readline())
words = []

for _ in range(N):
    word = sys.stdin.readline().rstrip() #문자를 입력받고 개행문자는 지움
    words.append(word) #리스트에 추가

words = list(set(words)) #중복된 문자를 지움
words.sort(key= lambda x : (len(x), x)) #길이로 먼저 정렬하고, 같다면 알파벳 오름차순으로 정렬

for i in words:
    print(i)