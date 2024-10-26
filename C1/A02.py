n, x = map(int, input().split())
a = list(map(int, input().split()))
print("Yes") if any(i == x for i in a) else print("No")

#-----------------
# n, x = map(int, input().split())
# def f(a):
#     for i in range(n):
#         if x == a[i]:
#             return 'Yes'
#     return 'No'
# print(f(list(map(int, input().split()))))
