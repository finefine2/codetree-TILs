import heapq
n = int(input())

q = []
for i in range(n):
    x = int(input())

    if x == 0 and len(q) >= 1:
        print(-heapq.heappop(q))
    elif x == 0 and len(q) == 0:
        print(0)
    else:
        heapq.heappush(q, -x)