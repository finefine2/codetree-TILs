n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

left = 0
right = n-1
ans = 0
arr.sort()

while left <= right:
    left_y, left_x = arr[left]
    right_y, right_x = arr[right]

    ans = max(ans, left_y + right_y)

    if left_x < right_x:
        arr[right] = (right_y, right_x - left_x)
        left += 1
    elif left_x > right_x:
        arr[left] = (left_y, left_x - right_x)
        right -= 1
    else:
        left += 1
        right -= 1

print(ans)

# 이진탐색 비슷하게 하는 거 같은데 사실 잘 모르겠다... 답을 참고함