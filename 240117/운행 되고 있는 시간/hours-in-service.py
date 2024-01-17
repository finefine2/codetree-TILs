n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

Max = -1
for i in range(n):
    arr2 = [0] * 1001

    for k in range(n):
        if i == k:
            continue
        a, b = arr[k]
        for l in range(a, b):
            arr2[l] += 1
    
    num = 0
    for k in range(1, 1000):
        if arr2[k] > 0:
            num += 1
    Max = max(Max, num)

print(Max)