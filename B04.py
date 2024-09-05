N = str(input())

binary = 0
for i in range(len(N)):
    binary += int(N[i]) * 2 ** (len(N) - 1 - i)
print(binary)
