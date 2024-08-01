import heapq

n, m = map(int, input().split())

q = []

for i in range(n):
    x, y = map(int, input().split())
    heapq.heappush(q, (abs(x) + abs(y), x, y))

for i in range(m):
    num, xx, yy = heapq.heappop(q)
    heapq.heappush(q, (abs(xx + 2) + abs(yy + 2), xx + 2, yy + 2))

num, xx, yy = heapq.heappop(q)
print(xx, yy)