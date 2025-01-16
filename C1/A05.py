n, k = map(int, input().split()) 

ans = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        x = k - i - j
        if x >= 1 and x <= n:
            ans += 1

print(ans)

#------------------
# N, K = map(int, input().split())

# c = 0
# for i in range(1, N+1):
#     for j in range(1, N+1):
#        s = K - i - j 
#        if N >= s and s >= 1:
#            c += 1

# print(c)
