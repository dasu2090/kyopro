a = 0
b = 0
ans = float('inf')  # 最大値を初期化 (C++の3000000000に相当)

# 再帰関数
def dfs(pos):
    global a, b, ans
    if pos == n:
        ans = min(ans, max(a, b))
        return
    
    a += k[pos]
    dfs(pos + 1)
    a -= k[pos]
    
    b += k[pos]
    dfs(pos + 1)
    b -= k[pos]

n = int(input())
k = list(map(int, input().split()))

dfs(0)
print(ans)
