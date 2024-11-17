# n = int(input())
# p = [0] * (n + 1)
# a = [0] * (n + 1)
# for i in range(n):
#     p[i], a[i] = map(int, input().split())
# dp = [[0] * (n+1) for _ in range(n+1)]

# for LEN in range(n - 1, -1, -1):
#     for l in range(LEN+1):
#         r = l + LEN - 1
#         score1 = 0
#         if l <= p[l-1] and p[l-1] <= r:
#             score1 = a[l-1]
#         score2 = 0
#         if l <= p[r+1] and p[r+1] <= r:
#             score2 = a[r+1]

#         if l == 1:
#             dp[l][r] = dp[l][r+1] + score2
#         elif r == n:
#             dp[l][r] = dp[l-1][r] + score1
#         else:
#             dp[l][r] = max(dp[l-1][r]+score1, dp[l][r+1] + score2)


# 入力
N = int(input())
P = [0] * (N + 1)
A = [0] * (N + 1)
for i in range(1, N+1):
    P[i], A[i] = map(int, input().split())

# 動的計画法（LEN は r-l の値)
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][N] = 0
for LEN in reversed(range(0, N-1)):
    for l in range(1, N-LEN+1):
        r = l + LEN

        # score1 の値（l-1 番目のブロックを取り除くときの得点）を求める
        score1 = 0
        if l>=2 and l<=P[l-1] and P[l-1]<=r:
            score1 = A[l-1]

        # score2 の値（r+1 番目のブロックを取り除くときの得点）を求める
        score2 = 0
        if r<=N-1 and l<=P[r+1] and P[r+1]<=r:
            score2 = A[r+1]

        # dp[l][r] を求める
        if l==1:
            dp[l][r] = dp[l][r+1] + score2
        elif r==N:
            dp[l][r] = dp[l-1][r] + score1
        else:
            dp[l][r] = max(dp[l-1][r] + score1, dp[l][r+1] + score2)

# Answer = 0
# for i in range(1, N+1):
#     Answer = max(Answer, dp[i][i])
[print(d) for d in dp]
