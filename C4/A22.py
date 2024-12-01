n = int(input())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

dp = [-1000000000] * (n+1)
dp[1] = 0
for i in range(1, n):
    dp[a[i]] = max(dp[a[i]], dp[i]+100)
    for j in range(1, len(dp)):
        if dp[j] != -1000000000:
            print(dp[j], end=',')
        else:
            print("  0", end=',')
    print("\na = ",a[i], "i = ", i)
    dp[b[i]] = max(dp[b[i]], dp[i]+150)
    for j in range(1, len(dp)):
        if dp[j] != -1000000000:
            print(dp[j], end=',')
        else:
            print("  0", end=',')
    print("\nb = ",b[i], "i = ", i, "\n--------------")
print(dp[n])
