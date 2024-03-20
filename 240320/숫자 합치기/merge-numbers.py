import heapq
n = int(input())

arr = list(map(int, input().split()))

arr.sort()
ans = 0
q = []

for k in arr:
    heapq.heappush(q, k)

while len(q) > 1:
    x1 = heapq.heappop(q)
    x2 = heapq.heappop(q)

    ans += (x1 + x2)
    heapq.heappush(q, x1 + x2)


print(ans)