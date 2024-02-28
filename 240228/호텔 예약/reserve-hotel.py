n = int(input())

arr = []
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))

point = []
for i, (s, e) in enumerate(arr):
    point.append((s, 1, i))
    point.append((e, -1, i))

point.sort()

ans = []
s = set()
start = 0
for x, v, idx in point:
    if v == 1:
        if not s:
            start = x

        s.add(idx)
    else:
        s.remove(idx)

        if not s:
            end = x
            ans.append(end - start)

print(len(ans))