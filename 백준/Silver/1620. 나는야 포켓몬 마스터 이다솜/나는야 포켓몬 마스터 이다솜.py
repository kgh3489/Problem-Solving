import sys

N, M = map(int, sys.stdin.readline().split())
pokemons = {}

for i in range(N):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[i+1] = pokemon #숫자가 key인 딕셔너리 생성
    pokemons[pokemon] = i+1 #문자가 key인 딕셔너리 생성

for j in range(M):
    qst = sys.stdin.readline().rstrip()
    if qst.isdigit(): #입력이 숫자라면
        print(pokemons[int(qst)])
    else: #입력이 문자라면
        print(pokemons[qst])