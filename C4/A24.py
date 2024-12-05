import bisect

def longest_increasing_subsequence(arr):
    lis = []
    for x in arr:
        pos = bisect.bisect_left(lis, x)
        if pos == len(lis):
            lis.append(x)  # 新しい要素を追加
        else:
            lis[pos] = x  # 置き換える
    return len(lis)

# 入力
n = int(input())
a = list(map(int, input().split()))

# 出力
print(longest_increasing_subsequence(a))
