#문자열과 내장함수

#대문자 소문자 변환
message="It is time"
print(message.upper())
print(message.lower())
print(message)

temp=message.upper()
print(temp.find('I')) #처음 발견된 인덱스 번호 호출
print(temp.count('T')) #개수를 반환
print(message[:2], message[3:7]) #슬라이싱

print(len(message)) #문자열 길이 반환
for i in range(len(message)):
    print(message[i], end="-")
print()

for x in message:
    print(x, end=":")
print()

for x in message:
    if x.isupper():
        print(x)
    elif x.islower():
        print(x, end='')
print()

for x in message:
    if x.isalpha(): #알파벳이면
        print(x, end="")
print()


temp='AZ'
for x in temp:
    print(ord(x)) #아스키번호 출력

temp=65
print(chr(temp)) #아스키번호 -> 문자로 출력
        

