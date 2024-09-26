def count_pairs(N, K, A):
    left = 0
    count = 0

    for right in range(N):
        # 左端が条件を満たすように調整
        while A[right] - A[left] > K:
            left += 1
        # rightとleftの間のペアの数をカウント
        print(left+1, right+1)
        count += (right - left)

    return count

# 入力例
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 結果を出力
print(count_pairs(N, K, A))
