n, x = map(int, input().split())
a = list(map(int, input().split()))

l = 1
m = 0
r = n
while(l <= r):
    m = (l + r) // 2
    if x == a[m]:
        break
    elif a[m] < x:
        l = m + 1
    elif a[m] > x:
        r = m - 1
print(m+1)

#--------------------

# n, x = map(int, input().split())
# a = list(map(int, input().split()))

# def f(l, r):
#     if l >= r:
#         return l
#     mid = (l + r) // 2 
#     if a[mid] < x:
#         return f(mid + 1, r)
#     if a[mid] == x:
#         return mid + 1
#     if a[mid] > x:
#         return f(l, mid)

# print(f(0, n - 1))


#----------------------

# n, x = map(int, input().split())
# a = list(map(int, input().split()))

# def b(low, high):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if a[mid] == x:
#         return mid + 1
#     elif a[mid] < x:
#         return b(mid + 1, high)
#     else:
#         return b(low, mid - 1)

# print(b(0, n - 1))

#----------------------------------
# import bisect

# print(bisect.bisect_left(a, x) + 1)


#----------------------------------
# import sys

# input = sys.stdin.read
# data = input().split()
# n = int(data[0])
# x = int(data[1])
# output = []
# for i in range(1, n + 1):
#     a = int(data[i + 1])
#     if a == x:
#         sys.stdout.write(str(i)+'\n')
#         break
