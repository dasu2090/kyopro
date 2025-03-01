import bisect

n = int(input())
a = list(map(int, input().split()))

tmp = a
b = list(set(a))
b.sort()

for i in range(n):
    print(bisect.bisect_right(b,tmp[i]), end=" ")
print()

# import bisect

# n = int(input())
# a = list(map(int, input().split()))

# s = list(set(a))
# s.sort()
# b = [0] * (n * 1)
# for i in range(n):
#     b[i] = bisect.bisect_right(s,a[i])

# for i in b:
#     print(i, end=" ")
# print()
