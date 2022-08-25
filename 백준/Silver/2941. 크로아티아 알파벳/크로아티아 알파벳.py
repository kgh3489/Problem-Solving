cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
cnt = 0
for i in cro:
    if i in a:
        k = a.count(i)
        cnt+=k
print(len(a)-cnt)
