def power(a, b, m):
    p = a
    answer = 1
    for i in range(30):  # 30ビットまで見る
        wari = (1 << i)  # 2のi乗
        #print(bin((b // wari) % 2))
        if (b // wari) % 2 == 1:  # bのi番目のビットが1なら
            answer = (answer * p) % m
        p = (p * p) % m  # a^(2^i) を更新
    return answer

a, b = map(int, input().split())
print(power(a, b, 1000000007))
