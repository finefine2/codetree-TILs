import heapq

n, m = map(int, input().split())
k = int(input())

arr = [[] for _ in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    arr[e].append((s, w))
    # 도착지점, 가중치

INF = int(1e9)
dist = [INF] * (n + 1)

q = []
dist[k] = 0
heapq.heappush(q, (0, k))

while q:
    min_dist, min_idx = heapq.heappop(q)

    if min_dist != dist[min_idx]:
        continue
    
    for tar_idx, tar_dist in arr[min_idx]:
        new_dist = dist[min_idx] + tar_dist
        
        if dist[tar_idx] > new_dist:
            dist[tar_idx] = new_dist
            heapq.heappush(q, (new_dist, tar_idx))

for i in range(1, n + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])