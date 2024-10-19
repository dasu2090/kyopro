n, k = map(int, input().split())
a = list(map(int, input().split()))

def c(m):
    ans = 0
    for i in range(n):
        ans += m // a[i]
    return ans

def f(l, r):
    if l >= r:
        return l
    mid = (l + r) // 2
    ans = c(mid)
    if ans > k:
        return f(l, mid)
    elif ans < k:
        return f(mid + 1, r)
    else:
        return mid

print(f(0, 10**9-1))

#----------------------

# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# def b(l, r):
#     if l >= r:
#         return r
#     sum = 0
#     m = (l + r) // 2
#     for i in range(n):
#         sum += m // a[i]
#         if sum >= k:
#             return b(l, m)
#     return b(m+1, r)

# print(b(1, 10**9))


#------------------------
# N, K = map(int, input().split())
# A = list(map(int, input().split()))

# def check(x):
#     sum = 0
#     for i in range(N):
#         sum += x // A[i]
#         if sum >= K:
#             return True
#     return False

# Left = 1
# Right = 10 ** 9
# while Left < Right:
#     Mid = (Left + Right) // 2
#     Answer = check(Mid)

#     if Answer == False:
#         Left = Mid + 1
#     if Answer == True:
#         Right = Mid
# print(Left)
