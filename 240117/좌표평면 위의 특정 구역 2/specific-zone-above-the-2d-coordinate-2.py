import sys
n = int(input())

ans = 0
Max = 0
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))


for i in range(n):
    Minx = sys.maxsize
    Miny = sys.maxsize 
    Maxx = 1
    Maxy = 1

    for k, (a, b) in enumerate(arr):
        if k == i:
            continue
        
        Minx = min(Minx, a)
        Miny = min(Miny, b)
        Maxx = max(Maxx, a)
        Maxy = max(Maxy, b)

    ans = min(ans, (Maxx - Minx) * (Maxy - Miny))

print(ans)