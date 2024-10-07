N, K = map(int, input().split())

c = 0
for i in range(1, N+1):
    for j in range(1, N+1):
       s = K - i - j 
       if N >= s and s >= 1:
           c += 1

print(c)
