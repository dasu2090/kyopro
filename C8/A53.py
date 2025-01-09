import heapq

q = int(input())
h = []

for _ in range(q):
    l = list(map(str, input().split()))
    if l[0] == '1':
        heapq.heappush(h, int(l[1]))
    elif l[0] == '2':
        print(heapq.nsmallest(1, h)[0])
    elif l[0] == '3':
        heapq.heappop(h)
