n, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(n)]

dp = [0] * (W + 1)

for weight, value in items:
    for w in range(W, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[W])

# N, W = map(int, input().split())

# w = [0] * (W+1)
# v = [0] * (W+1)
# for i in range(N):
#     w[i], v[i] = map(int, input().split())

# dp = [[0] * (W+1) for _ in range(N+1)]
# for i in range(N+1):
#     for j in range(W+1):
#         if j < w[i]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
# print(dp[N][W])
