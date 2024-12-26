n, m, b = map(int, input().split())

a = 0
c = 0
for i in list(map(int, input().split())):
    a += i

for i in list(map(int, input().split())):
    c += i

print((a * m) + (b * n * m) + (c * n))
