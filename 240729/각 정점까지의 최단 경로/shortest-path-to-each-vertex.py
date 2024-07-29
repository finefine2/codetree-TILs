import heapq

n, m = map(int, input().split())
k = int(input())

arr = [[] for _ in range(n+1)]
for i in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    arr[e].append((s, w))
    # 도착지점, 가중치
    # 양방향이 가능하므로 이렇게 두개를 다 넣어주어야 한다.

INF = int(1e9)
dist = [INF] * (n + 1)

q = []
dist[k] = 0
heapq.heappush(q, (0, k))
# 출발은 k이므로 거리를 0으로 해주고 큐에도 (0, k)로 넣어준다.

while q:
    min_dist, min_idx = heapq.heappop(q)
    # 큐에서 제일 작은 거리를 가진 것을 빼주고 각각 min_dist, min_idx로

    if min_dist != dist[min_idx]:
        continue
    # dist의 min_idx 값과 현재 값의 거리가 다른 경우에는 넘어간다.
    # 즉 같은 정점의 원소가 여러 번 문제가 나올 수 있어서 다를 경우에 넘어간다.
    
    # 최솟값에 해당하는 정점에 연결된 간선들을 기준으로 거리를 갱신
    for tar_idx, tar_dist in arr[min_idx]:
        new_dist = dist[min_idx] + target_dist
        
        # 현재 위치에서 연결된 간선으로 가는 것이 더 작으면 
        # 값을 갱신하고 우선순위 큐에 새로운 정보를 넣는다.
        if dist[tar_idx] > new_dist:
            dist[tar_idx] = new_dist
            heapq.heappush(q, (new_dist, tar_idx))

for i in range(1, n + 1):
    if dist[i] == INF:
        print(-1)
    else:
        print(dist[i])