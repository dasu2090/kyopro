n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

p = [0] * (n * n)
q = [0] * (n * n)
for i in range(n):
    for j in range(n):
        p[i*n+j] = a[i] + b[j]

for i in range(n):
    for j in range(n):
        q[i*n+j] = c[i] + d[j]

q.sort()
def b(ans, l, r):
    if l >= r:
        return False
    mid = (l + r) // 2
    if q[mid] == ans:
        return True
    if q[mid] < ans:
        return b(ans, mid+1, r)
    if q[mid] > ans:
        return b(ans, l, mid)

def f():
    for i in range(n*n):
        ans = k - p[i]
        if b(ans, 0, n*n-1):
            return "Yes"
    return "No"

print(f())

#--------------------------
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
# d = list(map(int, input().split()))

# p = [a[i] + b[j] for i in range(n) for j in range(n)]
# q = [c[i] + d[j] for i in range(n) for j in range(n)]

# q.sort()

# def binary(arr, target, left, right):
#     if left >= right:
#         return False
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return True
#     if arr[mid] < target:
#         return binary(arr, target, mid + 1, right)
#     if arr[mid] > target:
#         return binary(arr, target, left, mid)

# def f():
#     for x in p:
#         if binary(q, k - x, 0, len(p) - 1):
#             return "Yes"
#     return "No"

# print(f())


#--------------------------
#n, k = map(int, input().split())
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#c = list(map(int, input().split()))
#d = list(map(int, input().split()))

#p = [a[i] + b[j] for i in range(n) for j in range(n)]
#q = [c[i] + d[j] for i in range(n) for j in range(n)]

#def f():
#    for i in range(n*n):
#        for j in range(n*n):
#            if k - p[i] == q[j]:
#                return "Yes"
#    return "No"

#print(f())

