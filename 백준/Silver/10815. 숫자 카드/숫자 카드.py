N = int(input())
a = list(map(int, input().split()))
M = int(input())
b = list(map(int, input().split()))

a.sort() #이진 탐색을 위하여 탐색할 리스트 정렬

for i in b:
    start = 0 #첫 번째 인덱스
    end = len(a)-1 #마지막 인덱스
    
    while start <= end: #start와 end가 같아지면 모두 탐색한 것이므로 탐색 종료
        mid = (start+end) // 2 #바뀐 start, end에 따라 mid 값도 변경
        if i == a[mid]:
            print(1, end = " ")
            break
        elif i < a[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    else:
        print(0, end = " ")