import heapq
n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    arr[s].append((e, w))
    arr[e].append((s, w))

a, b = map(int, input().split())

INF = int(1e9)
dist = [INF] * (n + 1)
path = [0] * (n + 1)
q = []
heapq.heappush(q, (0, a))

dist[a] = 0
while q:
    min_dist, min_idx = heapq.heappop(q)

    if dist[min_idx] != min_dist:
        continue
    
    for tar_idx, tar_dist in arr[min_idx]:
        new_dist = dist[min_idx] + tar_dist

        if dist[tar_idx] > new_dist:
            dist[tar_idx] = new_dist
            heapq.heappush(q, (new_dist, tar_idx))
            path[tar_idx] = min_idx
            # 그때의 path의 tar_idx 값에 min_idx를 적어준다.
            # 즉 최소의 idx는 어디서 왔는지 기록하는 것

v = [b]
x = b
while x != a:
    x = path[x]
    v.append(x)
# 처음에 b부터 시작해서 x가 a가 될대 까지 해준다.
# path를 뒤에서부터 따라가며 v에 경로들을 저장해준다.

print(dist[b])
for k in v[::-1]:
    print(k, end = " ")