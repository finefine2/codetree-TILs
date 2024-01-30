n, t = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))


while True:

    if t == 0:
        break
    
    tmp = arr[-1]
    tmp2 = arr2[-1]
    tmp3 = arr3[-1]
    
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    
    for i in range(len(arr2)-1, 0, -1):
        arr2[i] = arr2[i-1]
    
    for i in range(len(arr3)-1, 0, -1):
        arr3[i] = arr3[i-1]
    
    arr[0] = tmp3
    arr2[0] = tmp
    arr3[0] = tmp2

    t -= 1

for k in arr:
    print(k, end = " ")
print()
for k in arr2:
    print(k, end = " ")
print()
for k in arr3:
    print(k, end = " ")