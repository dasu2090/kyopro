h, w = map(int, input().split())

x = [list(map(int, input().split())) for _ in range(h)]

for i in range(h):
    for j in range(1, w):
        x[i][j] += x[i][j - 1]

for i in range(1, h):
    for j in range(w):
        x[i][j] += x[i - 1][j]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    
    s = x[c - 1][d - 1]
    
    if a > 1:
        s -= x[a - 2][d - 1]
    if b > 1:
        s -= x[c - 1][b - 2]
    if a > 1 and b > 1:
        s += x[a - 2][b - 2]

    print(s)
