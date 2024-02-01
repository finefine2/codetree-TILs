n = int(input())

arr = list(map(str, input().split()))

ans = 0
for i in range(n):
    x = chr(ord('A') + i)

    idx = 0
    for j in range(n):
        if arr[j] == x:
            idx = j
            break
    
    for j in range(idx - 1, i - 1, -1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        ans += 1

print(ans)