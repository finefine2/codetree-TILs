arr = list(map(int, list(input())))

Max = -1
for i in range(len(arr)):
    arr[i] = 1 - arr[i]
    num = 0
    for j in range(len(arr)):
        num = num * 2 + arr[j]
    
    if Max < num:
        Max = num
    
    arr[i] = 1 - arr[i]

print(Max)