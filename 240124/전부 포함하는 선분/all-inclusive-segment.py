n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())    
    arr.append((a, b))

ans = 101
for i in range(n):
    Min = 101
    Max = 0
    for j in range(n):
        if i == j:
            continue

        Min = min(arr[j][0], Min)
        Max = max(arr[j][1], Max)
    
    ans = min(ans, Max - Min)

print(ans)