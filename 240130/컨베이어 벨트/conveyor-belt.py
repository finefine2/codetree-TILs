n, t = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

while True:

    if t == 0:
        break
    
    tmp = arr[-1]
    tmp2 = arr2[-1]
    
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    
    for i in range(len(arr2)-1, 0, -1):
        arr2[i] = arr2[i-1]
    
    arr[0] = tmp2
    arr2[0] = tmp

    t -= 1

for k in arr:
    print(k, end = " ")
print()
for k in arr2:
    print(k, end = " ")