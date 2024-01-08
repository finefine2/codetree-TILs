n = int(input())
arr = list(map(int, input().split()))

def two(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2
    # for k in arr:
    #     if k % 2 == 0:
    #         k //= 2
    
two(arr)

for k in arr:
    print(k, end = " ")