n, x = map(int, input().split())
def f(a):
    for i in range(n):
        if x == a[i]:
            return 'Yes'
    return 'No'
print(f(list(map(int, input().split()))))
