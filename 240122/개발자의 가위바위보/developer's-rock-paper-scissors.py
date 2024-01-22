n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

def find(num):
    if num == 1:
        return (1, 2, 3)
    elif num == 2:
        return (1, 3, 2)
    elif num == 3:
        return (2, 1, 3)
    elif num == 4:
        return (2, 3, 1)
    elif num == 5:
        return (3, 1, 2)
    else:
        return (3, 2, 1)

ans = 0
for k in range(6):
    a, b, c = find(i)
    cnt = 0
    for x, y in arr:
        if (x, y) in [(b, a), (c, b), (a, c)]:
            cnt += 1
        # (a, b), (b, c), (c, a)의 역순
    
    ans = max(cnt, ans)

print(ans)