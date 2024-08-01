import heapq
n = int(input())
arr = list(map(int, input().split()))


ans = 0
for k in range(1, n-1):
    q = arr[k:]
    heapq.heapify(q)
    heapq.heappop(q)
    # heapify 해주면 간단

    s = 0
    for l in q:
        s += l

    if len(q) != 0:
        ans = max(ans, s / len(q))

print(f"{ans:.2f}")