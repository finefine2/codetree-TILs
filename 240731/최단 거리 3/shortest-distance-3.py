import heapq
n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for i in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    arr[e].append((s, w))

a, b = map(int, input().split())

INF = int(1e9)
dist = [INF] * (n + 1)

dist[a] = 0
q = []
heapq.heappush(q, (0, a))

while q:
    distance, now = heapq.heappop(q)

    if dist[now] < distance:
        continue

    for tar_idx, tar_dist in arr[now]:
        new_dist = dist[now] + tar_dist

        if new_dist < dist[tar_idx]:
            dist[tar_idx] = new_dist
            heapq.heappush(q, (new_dist, tar_idx))

print(dist[b])