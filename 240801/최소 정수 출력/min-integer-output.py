import heapq
n = int(input())

q = []
for i in range(n):
    a = int(input())

    if a == 0 and len(q) >= 1:
        print(heapq.heappop(q))
    elif a == 0 and len(q) == 0:
        print(0)
    else:
        heapq.heappush(q, a)