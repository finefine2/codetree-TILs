n = int(input())

arr = list(map(int, input().split()))

tmp = [0] * n
for i in range(1, n+1):
    arr2 = [0] * n
    arr2[0] = i
    check = True

    for j in range(1, n):
        arr2[j] = (arr[j-1] - arr2[j-1])
        if not (1 <= arr2[j] <= n) and arr2[j] <= arr2[j-1]:
            check = False
            break
        
    if check and len(set(arr2)) == n:
        break
    
    
for i in range(n):
    print(arr2[i], end = " ")