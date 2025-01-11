q = int(input())

m = {}
for _ in range(q):
    l = list(map(str, input().split()))
    if l[0] == '1':
        m[l[1]] = l[2]
    elif l[0] == '2':
        print(m[l[1]])
