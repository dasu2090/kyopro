h, w = map(int, input().split())
grid = [[0] * (w+1) for _ in range(h+1)]

for y in range(1, h+1):
    tmp = list(map(int, input().split()))
    for x in range(1, w+1):
        grid[y][x] += tmp[x-1] + grid[y][x-1]
for y in range(2, h+1):
    for x in range(1, w+1):
        grid[y][x] += grid[y-1][x]

q = int(input())
for i in range(q):
    a, b, c, d = map(int, input().split())
    lu = grid[a-1][b-1]
    ld = grid[c][b-1]
    ru = grid[a-1][d]
    rd = grid[c][d]
    print(rd+lu-ld-ru)

# h, w = map(int, input().split())
# grid = [[0] * (w + 1) for _ in range(h + 1)]

# for y in range(1, h + 1):
#     tmp = list(map(int, input().split()))
#     for x in range(1, w + 1):
#         grid[y][x] += tmp[x - 1] + grid[y][x - 1]
# for y in range(2, h + 1):
#     for x in range(1, w + 1):
#         grid[y][x] += grid[y - 1][x]

# q = int(input())
# for i in range(q):
#     a, b, c, d = map(int, input().split())
#     lu = grid[a - 1][b - 1]
#     ld = grid[c][b - 1]
#     ru = grid[a - 1][d]
#     rd = grid[c][d]
#     print(rd + lu - ld - ru)


# h, w = map(int, input().split())
# x = [list(map(int, input().split())) for _ in range(h)]

# for i in range(h):
#     for j in range(1, w):
#         x[i][j] += x[i][j - 1]

# for i in range(1, h):
#     for j in range(w):
#         x[i][j] += x[i - 1][j]

# q = int(input())
# for _ in range(q):
#     a, b, c, d = map(int, input().split())
    
#     s = x[c - 1][d - 1]
    
#     if a > 1:
#         s -= x[a - 2][d - 1]
#     if b > 1:
#         s -= x[c - 1][b - 2]
#     if a > 1 and b > 1:
#         s += x[a - 2][b - 2]

#     print(s)
