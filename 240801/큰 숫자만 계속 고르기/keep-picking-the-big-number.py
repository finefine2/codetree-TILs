import heapq

n, m = map(int, input().split())

q = []
arr = list(map(int, input().split()))
for a in arr:
    heapq.heappush(q, -a)

for i in range(m):
    num = heapq.heappop(q)
    num = num + 1
    heapq.heappush(q, num)

print(-heapq.heappop(q))