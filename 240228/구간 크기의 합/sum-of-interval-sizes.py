n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())

    arr.append((a, b))

point = []
for i, (a, b) in enumerate(arr):
    point.append((a, 1, i))
    point.append((b, -1, i))

point.sort()
s = set()

ans = 0
start = -1
end = 0
for x, v, idx in point:
    if v == 1:
        if not s:
            start = x 

        s.add(idx)
    else:
        s.remove(idx)

        if not s:
            end = x
            ans += (end - start)

print(ans)