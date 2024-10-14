n, x = map(int, input().split())
a = list(map(int, input().split()))

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
