a, b = map(int, input().split())

def f():
    for i in range(a, b+1):
        if (100 / i) - (100 // i) == 0:
            return "Yes"
    return "No"

print(f())
