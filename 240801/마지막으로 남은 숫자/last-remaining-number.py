import heapq

q = []

n = int(input())
arr = list(map(int, input().split()))

for k in arr:
    heapq.heappush(q, -k)

while len(q) >= 2:
    num1 = -heapq.heappop(q)
    num2 = -heapq.heappop(q)

    if num1 != num2:
        heapq.heappush(q, -abs(num1 - num2))

if len(q) == 0:
    print(-1)
else:
    print(-heapq.heappop(q))