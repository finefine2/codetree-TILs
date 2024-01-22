n = int(input())



arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

check = False
for i in range(len(arr)):
    Max = -1
    Min = 101
    for j in range(len(arr)):
        if i == j:
            continue
        Max = max(Max, arr[j][0])
        Min = min(Min, arr[j][1])
    if Max <= Min:
        check = True

if check:
    print("Yes")
else:
    print("No")