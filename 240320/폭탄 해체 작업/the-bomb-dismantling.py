import heapq
n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((b, a))

arr.sort()

q = []
idx = n-1
ans = 0

for t in range(10000, 0, -1):
    while idx >= 0 and arr[idx][0] >= t:
        heapq.heappush(q, -arr[idx][1])
        idx -= 1
    
    if q:
        ans += -heapq.heappop(q)


print(ans)