n, k = map(int, input().split())
a = list(map(int, input().split()))

c = 0
j = 0
for i in range(n):
    while j < n and a[j] - a[i] <= k:
        j += 1
    print(i+1, j)
    c += j - i - 1
print(c)


#--------------------------------
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# count = 0
# j = 0

# for i in range(n):
#     while j < n and a[j] - a[i] <= k:
#         j += 1
#     print(j, i, j - i - 1)
#     count += j - i - 1
# print(count)

#--------------------------------
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# left = 0
# count = 0

# for right in range(N):
#     while A[right] - A[left] > K:
#         left += 1
#     print(left+1, right+1)
#     count += (right - left)

# print(count)
