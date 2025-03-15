n, q = map(int, input().split())
a = list(map(int, input().split()))

b = [0] * (n + 1)
for i in range(n):
    b[i + 1] = b[i] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(b[r] - b[l - 1])

# print(b)

# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# b = [0] * (n+1)
# b[1] = a[0]
# for i in range(2, n+1):
#     b[i] = a[i-1] + b[i-1]

# for _ in range(q):
#     l, r = map(int, input().split())
#     print(b[r]-b[l-1])
# print(b)


# n, q = map(int, input().split())
# a = list(map(int, input().split()))

# for i in range(1, n):
#     a[i] += a[i - 1]
# for _ in range(q):
#     l, r = map(int, input().split())
#     if l != 1:
#         print(a[r - 1] - a[l - 2])
#     else:
#         print(a[r - 1])


# N, Q = map(int, input().split())
# A = list(map(int, input().split()))

# S = [0] * (N + 1)
# for i in range(N):
#     S[i+1] = S[i] + A[i]

# for _ in range(Q):
#     L, R = map(int, input().split())
#     print(S[R] - S[L - 1])
