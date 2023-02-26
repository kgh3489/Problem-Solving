dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
cnt = 0
for i in a:
    for j in dial:
        if i in j:
            cnt += dial.index(j)+3
print(cnt)