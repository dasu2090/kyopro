n, q = map(int, input().split())
a = list(map(int, input().split()))
for i in range(1, n):
    a[i] += a[i - 1]
for i in range(q):
    l, r = map(int, input().split())
    print(a[r - 1] - a[l - 2])

N, Q = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i+1] = S[i] + A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    print(S[R] - S[L - 1])
