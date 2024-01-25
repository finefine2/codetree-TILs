n = int(input())

arr = list(map(int, input().split()))

check = False
while not check:
    check = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            check = False


for k in arr:
    print(k, end = " ")