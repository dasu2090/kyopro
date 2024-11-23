def solve():
    # 入力
    N, M = map(int, input().split())
    coupons = []
    for _ in range(M):
        coupons.append(list(map(int, input().split())))

    # ビットDPの初期化
    INF = float('inf')
    dp = [INF] * (1 << N)
    dp[0] = 0

    # DP更新
    for coupon in coupons:
        # クーポンでカバーされる商品をビットで表現
        coverage = 0
        for i in range(N):
            if coupon[i] == 1:
                coverage |= (1 << i)
        
        # 状態を更新
        for bit in range(1 << N):
            dp[bit | coverage] = min(dp[bit | coverage], dp[bit] + 1)

    # 最終的な全ての商品をカバーする状態を確認
    answer = dp[(1 << N) - 1]
    print(answer if answer != INF else -1)

solve()
