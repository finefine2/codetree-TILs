n, k = map(int, input().split())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

left = 0
right = n-1
ans = 0

while left < right:
    if arr[left] + arr[right] <= k:
        ans += (right - left)
        left += 1
    else:
        right -= 1

print(ans)