n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [float('inf')] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    dp[i] = min(dp[i], dp[i - 1] + a[i - 2])
    if i > 2:
        dp[i] = min(dp[i], dp[i - 2] + b[i - 3])

print(dp[n])
#------------------------
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# dp = [0] * (n + 1)
# dp[2] = a[0]

# for i in range(3, n+1):
#     dp[i] = min(dp[i-1] + a[i-2], dp[i-2] + b[i-3])

# print(dp[n])

#---------------------------
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# dp = [0] * (n + 1)
# dp[2] = a[0]

# for i in range(3, n + 1):
#     dp[i] = min(dp[i - 1] + a[i - 2], dp[i - 2] + b[i - 3])

# print(dp[n])

#----------------------------
# n = int(input())
# at = list(map(int, input().split()))
# bt = list(map(int, input().split()))
# a = {}
# b = {}
# for i in range(2, n + 1):
#     a[i] = at[i - 2]
# for i in range(3, n + 1):
#     b[i] = bt[i - 3]

# dp = [0] * (n + 1)
# dp[1] = 0
# dp[2] = a[2]
# for i in range(3, n + 1):
#     dp[i] = min(dp[i - 1] + a[i], dp[i - 2] + b[i])

# print(dp[n])
