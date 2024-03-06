n, m = map(int, input().split())

arr = list(map(int, input().split()))


left = 0
right = 0
ans = 0
s = arr[0]

while True:
    if s > m:
        s -= arr[left]
        left += 1
    elif s == m:
        ans += 1
        s -= arr[left]
        left += 1
    else:
        right += 1
        if right == n:
            break
        s += arr[right]

print(ans)