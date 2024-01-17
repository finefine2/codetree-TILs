n = int(input())

arr = []
for i in range(n):
    a, b, c = map(int, input().split())
    arr.append((a, b, c))

Max = 0
ans = 0
for i in range(1, 4):
    num = 0
    idx = i
    for j in range(n):
        if arr[j][0] == idx:
            idx = arr[j][1]
            
        elif arr[j][1] == idx:
            idx = arr[j][0]
            
        if arr[j][2] == idx:
            num += 1
    
    if Max < num:
        Max = num
        ans = i

print(ans)