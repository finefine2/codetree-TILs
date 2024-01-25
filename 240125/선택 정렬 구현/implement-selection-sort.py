n = int(input())

arr = list(map(int, input().split()))

for i in range(n):
    Min = i
    for j in range(i+1, n):
        if arr[j] < arr[Min]:
            Min = j
    arr[i], arr[Min] = arr[Min], arr[i]
    
for k in arr:
    print(k, end = " ")