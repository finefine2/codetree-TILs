import heapq
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    # s에서 e로 가는 비용이 w

INF = int(1e9)
dist = [INF] * (n + 1)

q = []
heapq.heappush(q, (0, 1))
dist[1] = 0
# 처음 시작점이 1이므로 시작인 1로 가는 것은 0으로 설정한다.
# 또한 시작점이 1인 dist도 0으로 해주고 시작한다.

while q:
    distance, now = heapq.heappop(q)
    
    if dist[now] < distance:
        continue
    # 지금 현재의 거리가 더 클 경우에는 할 필요가 없다.

    for next in arr[now]:
        cost = distance + next[1]

        if cost < dist[next[0]]:
            dist[next[0]] = cost
            heapq.heappush(q, (cost, next[0]))

for i in range(2, n+1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])