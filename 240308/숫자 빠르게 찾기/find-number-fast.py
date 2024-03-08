n, m = map(int, input().split())

arr = list(map(int, input().split()))

def find(arr, num):
    idx = -1
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == num:
            idx = mid
            break
        
        if arr[mid] > num:
            right = mid - 1
        else:
            left = mid + 1
    
    if idx == -1:
        return -1
    else:
        return idx + 1

for i in range(m):
    a = int(input())
    print(find(arr, a))