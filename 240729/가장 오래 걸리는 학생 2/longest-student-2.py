import heapq
n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
INF = int(1e9)
dist = [INF] * (n + 1)

for i in range(m):
    i, j, d = map(int, input().split())
    arr[j].append((i, d))

q = []
dist[n] = 0
heapq.heappush(q, (0, n))

while q:
    min_dist, min_idx = heapq.heappop(q)

    if dist[min_idx] != min_dist:
        continue
    
    # arr에서의 순서는 인덱스, dist이다.
    for tar_idx, tar_dist in arr[min_idx]:
        new_dist = dist[min_idx] + tar_dist

        if dist[tar_idx] > new_dist:
            dist[tar_idx] = new_dist
            heapq.heappush(q, (new_dist, tar_idx))



ans = 0
for i in range(1, n):
    if dist[i] != INF:
        ans = max(ans, dist[i])

print(ans)