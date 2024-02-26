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
for x, v, idx in point:
    if v == 1:
        if not s:
            ans += 1
        # 남아있는 선분이 없으면 ans 늘려준다.

        s.add(idx)
        # 해당 선 번호를 set에 넣는다.
    else:
        s.remove(idx)

print(ans)