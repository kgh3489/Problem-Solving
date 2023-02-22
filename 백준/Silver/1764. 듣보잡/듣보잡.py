import sys

input = sys.stdin.readline

N, M = map(int, input().split())
# set 자료형으로 변환
d = set([input().rstrip() for _ in range(N)])
b = set([input().rstrip() for _ in range(M)])

d_b = sorted(list(d & b)) #d와 b의 교집합을 구한 후 다시 리스트로 변환하여 정렬

print(len(d_b))
for i in d_b:
    print(i)
