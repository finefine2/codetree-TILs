n = int(input())

arr = list(map(int, input().split()))

arr.sort()

left = 0
right = n-1

ans = abs(arr[left] + arr[right])

while left <= right:
    s = arr[left] + arr[right]

    if abs(s) < ans:
        ans = abs(s)

    if s > 0:
        right -= 1
    elif s < 0:
        left += 1
    else:
        break

print(ans)