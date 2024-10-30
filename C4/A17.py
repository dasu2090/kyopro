n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * (n + 1)
dp[2] = a[0]
for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i - 2], dp[i - 2] + b[i - 3])

p = n
ans = []
def f(ans, p):
    ans.append(p)
    if p == 1:
        return
    if dp[p - 1] + a[p - 2] == dp[p]:
        return f(ans, p - 1)
    else:
        return f(ans, p - 2)

f(ans, p)
print(len(ans))
for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end=' ')
print()
#------------------
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# dp = [0] * (n + 1)
# dp[2] = a[0]
# for i in range(3, n + 1):
#     dp[i] = min(dp[i - 1] + a[i - 2], dp[i - 2] + b[i - 3])

# p = n
# ans = []
# while True:
#     ans.append(p)
#     if p == 1:
#         break
#     if dp[p - 1] + a[p - 2] == dp[p]:
#         p = p - 1
#     else:
#         p = p - 2

# print(len(ans))
# for i in range(len(ans) - 1, -1, -1):
#     print(ans[i], end=' ')
# print()

