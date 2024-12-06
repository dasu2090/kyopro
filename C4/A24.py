import bisect

def lis_length(n, array):
    dp = []  # 最長増加部分列の候補を管理する配列
    for num in array:
        # num を挿入すべき位置を二分探索で見つける
        pos = bisect.bisect_left(dp, num)
        if pos == len(dp):
            dp.append(num)  # 新しい要素を追加
        else:
            dp[pos] = num  # 既存の要素を置き換え
    return len(dp)

# 入力例
n = 6
array = [2, 3, 1, 6, 4, 5]

# 出力
print(lis_length(n, array))  # 出力例: 4
