n = int(input())
for i in range(9,-1, -1):
    d = 1 << i
    print((n // d) % 2, end='')
print()

#-------------------
# n = int(input())

# for i in range(9, -1, -1):
#     if n & (1 << i):
#         print(1, end='')
#     else:
#         print(0, end='')
# print()
