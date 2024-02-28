import heapq

n = int(input())

arr = []
for i in range(n):
    p, q = map(int, input().split())
    arr.append((p, q))

computer = []
for i in range(1, n+1):
    heapq.heappush(computer, i)

point = []
for i, (a, b) in enumerate(arr):
    point.append((a, 1, i))
    point.append((b, -1, i))

point.sort()

num = [0] * (n+1)
for x, v, idx in point:
    if v == 1:
        cnt = heapq.heappop(computer)
        num[idx] = cnt
    else:
        cnt = num[idx]
        heapq.heappush(computer, cnt)

for k in num:
    print(k, end = " ")