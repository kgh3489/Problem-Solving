# 합이 같은 부분집합

# import sys
# sys.stdin=open("input.txt", "r")

def DFS(L, sum): # 레벨, 누적
    if sum > total//2: # 합이 절반을 넘으면 종료
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # 프로그램 종료
    else:
        DFS(L+1, sum+a[L]) # 요소를 더하고 재귀
        DFS(L+1, sum) # 요소를 더하지 않고 재귀
    

if __name__=="__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")

