n = int(input())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

point = []
for (s, e) in arr:
    point.append((s, 1))
    point.append((e, -1))

point.sort(key = lambda x : (x[0], -x[1]))



ans = 0
s = 0
for x, v in point:
    s += v
    ans = max(ans, s)

print(ans)