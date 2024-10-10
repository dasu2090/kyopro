h, w, n = map(int, input().split())

z = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(n):
    a, b, c, d = map(int, input().split())
    z[a][b] += 1
    z[a][d + 1] -= 1
    z[c + 1][b] -= 1
    z[c + 1][d + 1] += 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        z[i][j] += z[i][j - 1]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        z[i][j] += z[i - 1][j]

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(z[i][j], end=' ')
    print()
