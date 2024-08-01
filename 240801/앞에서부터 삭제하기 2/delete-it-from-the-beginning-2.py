import heapq
n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)

ans = 0
for k in range(1, n-1):
    q = arr[k:]
    heapq.heapify(q)
    small = heapq.heappop(q)
    # heapify 해주면 간단

    s = total - sum(arr[:k]) - small

    if len(q) != 0:
        ans = max(ans, s / len(q))

print(f"{ans:.2f}")