q = int(input())

def f(x):
    i = 2
    while i * i <= x:
        if x % i == 0:
            return "No"
        i = i + 1
    return "Yes"

for _ in range(q):
    print(f(int(input())))
