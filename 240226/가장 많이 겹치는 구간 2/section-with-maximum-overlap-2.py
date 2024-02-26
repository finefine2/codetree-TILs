n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    
point = []
for a, b in arr:
    point.append((a, 1))
    point.append((b, -1))

point.sort()

ans = []
s = 0
for x, v in point:
    if x >= 1000000000:
        break
    
    s += v
    ans.append(s)

print(max(ans))