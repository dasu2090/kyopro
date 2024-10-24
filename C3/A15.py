import bisect

n = int(input())
a = list(map(int, input().split()))

s = list(set(a))
b = [0] * (n * 1)
for i in range(n):
    b[i] = bisect.bisect_right(s,a[i])

# print(s)
# print(a)
print(b)
