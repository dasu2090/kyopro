d = int(input())
n = int(input())

a = [0] * (d + 2)
for _ in range(n):
    l, r = map(int, input().split())
    a[l] += 1
    a[r + 1] -= 1

for i in range(1, d + 1):
    print(a[i])
    a[i + 1] += a[i]


# d = int(input())
# n = int(input())

# a = [0] * (d)
# for i in range(n):
#     l, r = map(int, input().split())
#     a[l - 1] += 1
#     a[r] -= 1
# s = 0
# for i in range(d):
#     s += a[i]
#     print(s)
