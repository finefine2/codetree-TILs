n = int(input())
arr = list(map(int, input().split()))

ans = merge_sort(arr, min(arr), max(arr))
print(*ans)


def merge_sort(arr[], low, high)
  if low < high
    mid = (low + high) / 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)


merged_arr = []

function merge(arr[], low, mid, high)
  i = low, j = mid + 1

  k = low
  while i <= mid && j <= high
    if arr[i] <= arr[j]
      merged_arr[k] = arr[i]
      k += 1; i += 1
    else
      merged_arr[k] = arr[j]
      k += 1; j += 1
  
  while i <= mid
    merged_arr[k] = arr[i]
    k += 1; i += 1

  while j <= high
    merged_arr[k] = arr[j]
    k += 1; j += 1
  
  for k = low ... k <= high
    arr[k] = merged_arr[k]
  
  return arr