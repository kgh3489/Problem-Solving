#제곱근과 제곱근을 정수까지 나타낸 수와 같다면 n은 양의 정수 x의 제곱
import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return (math.sqrt(n)+1)**2
    else:
        return -1