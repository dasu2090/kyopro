def min_coupons(M, N, coupons):
    INF = float('inf')
    dp = [[INF] * (1 << N) for _ in range(M + 1)]
    dp[0][0] = 0  # 初期状態: 空集合はクーポン0枚で無料

    for i in range(1, M + 1):
        T_i = coupons[i - 1]  # クーポンで無料になる品物の集合
        for S in range(1 << N):
            # クーポンを使わない場合
            dp[i][S] = dp[i - 1][S]
            # クーポンを使う場合
            dp[i][S | T_i] = min(dp[i][S | T_i], dp[i - 1][S] + 1)

    # 最後の状態で全品物を無料にする最小クーポン数
    return dp[M][(1 << N) - 1]

# 入力例
M = 4  # クーポンの数
N = 3  # 品物の数
coupons = [
    0b001,  # 品物1だけ無料
    0b010,  # 品物2だけ無料
    0b011,  # 品物1,2が無料
    0b100,  # 品物3だけ無料
]

J, I = map(int, input().split())

A = [[0] * (J) for _ in range(I)]

print(A)
# for i in range(I):
# print(min_coupons(M, N, coupons))  # 出力例: 2
