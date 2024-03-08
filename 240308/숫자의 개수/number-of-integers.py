n, m = map(int, input().split())
arr = list(map(int, input().split()))

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
        


for i in range(m):
    a = int(input())
    left = lower_bound(arr, a)
    right = upper_bound(arr, a)
    print(right - left)