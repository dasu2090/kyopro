q = int(input())

s = []
for _ in range(q):
    l = list(map(str, input().split()))
    if l[0] == '1':
        s.append(l[1])
    elif l[0] == '2':
        print(s[0])
    elif l[0] == '3':
        s.pop(0)
