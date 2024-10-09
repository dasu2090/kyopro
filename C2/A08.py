h, w = map(int, input().split())

x = [None] * h
for i in range(h):
    x[i] = list(map(int, input().split()))

q = int(input())
y = [None] * q
for i in range(q):
    y[i] = list(map(int, input().split()))

for i in range(h):
    for j in range(1, w):
        x[i][j] += x[i][j - 1]
for i in range(1, h):
    for j in range(w):
        x[i][j] += x[i - 1][j]

for i in range(q):
    a = y[i][0]
    b = y[i][1]
    c = y[i][2]
    d = y[i][3]
    s = x[c - 1][d - 1]

    if a >= 2 and b >= 2:
        s += x[a - 2][b - 2]
    if b >= 2:
        s -= x[c - 1][b - 2]
    if a >= 2:
        s -= x[a - 2][d - 1]
    print(s)
