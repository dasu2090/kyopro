n = str(input())

num = 0
for i in range(len(n)):
    num += 2 ** (len(n) - 1 - i) * int(n[i])
print(num)

# N = str(input())

# binary = 0
# for i in range(len(N)):
#     binary += int(N[i]) * 2 ** (len(N) - 1 - i)
# print(binary)
