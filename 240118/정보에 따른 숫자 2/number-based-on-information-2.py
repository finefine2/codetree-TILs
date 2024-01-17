t, a, b = map(int, input().split())

arr = [0] * 1001
for i in range(t):
    c, x = map(str, input().split())
    if c == 'S':
        arr[int(x)] = 1
    else:
        arr[int(x)] = 2

ans = 0
for i in range(a, b+1):
    for j in range(1000):
        if i - j >= 0 and i + j < 1000:
            if arr[i-j] == 1 or arr[i+j] == 1:
                ans += 1
                break
            elif arr[i-j] == 2 or arr[i+j] == 2:
                break
        elif i - j >= 0 and i + j >= 1000:
            if arr[i-j] == 1:
                ans += 1
                break
            elif arr[i-j] == 2:
                break
        elif i - j < 0 and i + j < 1000:
            if arr[i+j] == 1:
                ans += 1
                break
            elif arr[i+j] == 2:
                break

print(ans)