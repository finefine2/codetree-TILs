n, m = map(int, input().split())

arr = [0] + list(map(int, input().split()))
que = list(map(int, input().split()))

def find(num):
    left = 1
    right = n
    Min = n + 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= num:
            right = mid - 1
            Min = min(Min, mid)
        else:
            left = mid + 1

    return Min

for k in que:
    if find(k) <= n and arr[find(k)] == k:
        print(find(k))
    else:
        print(-1)