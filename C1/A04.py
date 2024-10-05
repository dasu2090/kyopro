n = int(input())
for i in range(9,-1, -1):
    d = 1 << i
    print((n // d) % 2, end='')
print()
