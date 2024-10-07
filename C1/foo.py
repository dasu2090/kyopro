n, k = map(int, input().split())

c = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        s = k - i - j
        if s <= n and s >= 1:
            c += 1
print(c)
