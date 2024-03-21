from sortedcontainers import SortedSet

c, n = map(int, input().split())

red = []
for i in range(c):
    a = int(input())
    red.append(a)

black = []
for i in range(n):
    a, b = map(int, input().split())
    black.append((a, b))

ans = 0
red_sort = SortedSet(red)
black.sort()

for a, b in black:
    idx = red_sort.bisect_left(a)
    
    if idx != len(red_sort):
        t = red_sort[idx]

        if t <= b:
            ans += 1
            red_sort.remove(t)

print(ans)