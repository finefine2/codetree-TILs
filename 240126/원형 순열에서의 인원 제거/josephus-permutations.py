from collections import deque


n, k = map(int, input().split())

arr = []
q = deque(range(1, n+1))

while len(q) > 1:
    for i in range(1, k):
        q.append(q.popleft())
    remove = q.popleft()
    arr.append(remove)
arr.append(q[0])

print(" ".join(map(str, arr)))