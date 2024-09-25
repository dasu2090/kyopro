n = int(input())

ans = 0
for _ in range(n):
    t, a = map(str, input().split())
    if t == '+':
        ans = ans + int(a)
    elif t == '-':
        ans = ans - int(a)
    elif t == '*':
        ans = ans * int(a)
    if ans < 0:
        ans += 10000
    ans %= 10000
    print(ans)
