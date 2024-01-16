n = int(input())

arr = [0] * 101
for i in range(n):
    a, b = map(str, input().split())
    if b == 'G':
        arr[int(a)] = 1
    else:
        arr[int(a)] = 2

Max = 0
for i in range(101):
    for j in range(i+1, 101):
        if arr[i] == 0 or arr[j] == 0:
            continue

        g = 0
        h = 0

        for k in range(i, j+1):
            if arr[k] == 1:
                g += 1
            if arr[k] == 2:
                h += 1

        if h == 0 or g == 0 or(h == g):
            Max = max(Max, j-i)

print(Max)