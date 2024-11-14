s = str(input())
t = str(input())

sl = len(s)
tl = len(t)
dp = [[0]*(tl+1) for _ in range(sl+1)]
for i in range(sl+1):
    for j in range(tl+1):
        if i > 0 and j > 0 and s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
        elif i > 0 and j > 0:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i > 0:
            dp[i][j] = dp[i-1][j]
        elif j > 0:
            dp[i][j] = dp[i][j-1]

print(" ", end=" ")
for a in s:
    print(a, end=" ")
print()
for i in range(1, tl+1):
    if i > 0:
        print(t[i-1], end=" ")
    for j in range(1, sl+1):
        print(dp[j][i], end=" ")
    print()
print()

#---------------
# S = input()
# T = input()

# N = len(S)
# M = len(T)

# dp = [[0] * (M + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         if S[i - 1] == T[j - 1]:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# print(dp[N][M])
