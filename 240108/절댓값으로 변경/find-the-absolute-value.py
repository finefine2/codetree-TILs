n = int(input())

arr = list(map(int, input().split()))

def func(arr):
    for i in range(len(arr)):
        if arr[i] <= 0:
            arr[i] *= -1

func(arr)

for k in arr:
    print(k, end = " ")