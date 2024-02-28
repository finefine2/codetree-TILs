from sortedcontainers import SortedSet


n = int(input())

arr = []
for i in range(n):
    y, x1, x2 = map(int, input().split())
    arr.append((y, x1, x2))


check = [0] * n
point = []
for i in range(n):
    y, a, b = arr[i]
    point.append((a, 1, i, y))
    point.append((b, -1, i, y))

point.sort()

s = SortedSet()
for x, v, idx, y in point:
    if v == 1:
        s.add((y, idx))
    else:
        s.remove((y, idx))
    
    if not s:
        continue
    
    k, k_idx = s[0]
    check[k_idx] = 1

ans = 0
for i in range(n):
    if check[i]:
        ans += 1

print(ans)