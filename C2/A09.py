h, w, n = map(int, input().split())
grid = [[0] * (w + 1) for h in range(h + 1)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    grid[a - 1][b - 1] += 1
    grid[a - 1][d] -= 1
    grid[c][b - 1] -= 1
    grid[c][d] += 1

for y in range(h):
    for x in range(1, w):
        grid[y][x] += grid[y][x - 1]

for y in range(1, h):
    for x in range(w):
        grid[y][x] += grid[y - 1][x]

for y in range(h):
    for x in range(w):
        if x >= 1:
            print(' ', end='')
        print(grid[y][x], end='')
    print('')


# h, w, n = map(int, input().split())
# z = [[0] * (w + 2) for _ in range(h + 2)]

# for i in range(n):
#     a, b, c, d = map(int, input().split())
#     z[a][b] += 1
#     z[a][d + 1] -= 1
#     z[c + 1][b] -= 1
#     z[c + 1][d + 1] += 1

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         z[i][j] += z[i][j - 1]

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         z[i][j] += z[i - 1][j]

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         print(z[i][j], end=' ')
#     print()
