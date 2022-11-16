from collections import deque

n = int(input())
cards = [i for i in range(1, n+1)] #1~n의 리스트를 만듦
cards = deque(cards) #리스트를 deque로 변환

while len(cards) > 1: #카드가 한 개 남을 때까지 반복
    cards.popleft() #제일 위에 있는 카드를 버림
    cards.append(cards[0]) #그 다음 위에 있는 카드를 밑으로 보냄
    cards.popleft() #그 숫자는 삭제

print(cards[0])
