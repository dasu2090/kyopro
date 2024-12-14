MOD = 10000

def process_operations(operations):
    current_value = 0
    results = []
    for operation in operations:
        op, value = operation
        value = int(value)
        if op == '+':
            current_value += value
        elif op == '-':
            current_value -= value
        elif op == '*':
            current_value *= value
        current_value %= MOD
        results.append(current_value)
    return results

operations = [
    ('+', 57),
    ('+', 43),
    ('*', 100),
    ('-', 1)
]

results = process_operations(operations)

for result in results:
    print(result)

#-------------------------------
n = int(input())

ans = 0
for _ in range(n):
    t, a = map(str, input().split())
    if t == '+':
        ans = ans + int(a)
    elif t == '-':
        ans = ans - int(a)
    elif t == '*':
        ans = ans * int(a)
    if ans < 0:
        ans += 10000
    ans %= 10000
    print(ans)
