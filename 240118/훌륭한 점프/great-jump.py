import sys
n, k = map(int, input().split())

arr = list(map(int, input().split()))

def move(num):
    arr2 = []
    for idx, cnt in enumerate(arr):
        if cnt <= num:
            arr2.append(idx)

    for i in range(1, len(arr2)):
        dist = arr2[i] - arr2[i-1]
        if dist > k:
            return False
    return True
    
Max = -1
Min = sys.maxsize
for i in range(max(arr[0], arr[-1]), 101):
    if move(i):
        Min = min(Min, i)

print(Min)