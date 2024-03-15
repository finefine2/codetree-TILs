n, m = map(int, input().split())

arr = list(map(int, input().split()))

def lower_bound(arr, num):
    left = 0
    right = n - 1
    idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= num:
            left = mid + 1
        else:
            right = mid - 1
            idx = min(idx, mid)

    return idx


def upper_bound(arr, num):
    left, right = 0, n - 1
    idx = n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid - 1
            idx = min(idx, mid)
        else:
            left = mid + 1

    return idx

arr.sort()
for i in range(m):
    a, b = map(int, input().split())
    
    s = lower_bound(arr, a)
    e = upper_bound(arr, b)

    print(e - s)