n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(s + 1):
        if j < a[i - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] or dp[i - 1][j - a[i - 1]]

if dp[n][s]:
    print("Yes")
else:
    print("No")

#---------------------
# n, s = map(int, input().split())
# a = list(map(int, input().split()))

# c = 0
# def f():
#     for i in range(1 << n):
#         c = 0
#         for j in range(n):
#             if i & (1 << j):
#                 c += a[j]
#         if c == s:
#             return "Yes"
#     print("No")
# print(f())
