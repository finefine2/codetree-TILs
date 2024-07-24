n = int(input())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((y, x))

# 합이 제일 큰 두 수가 있을때, 이 합이 최소가 되게
# y가 x번

ans = 0
left = 0
right = n-1
arr.sort()
# y, 즉 값들에 대해서 정렬해준다.

while left <= right:
    left_y ,left_x = arr[left]
    right_y, right_x = arr[right]

    ans = max(ans, right_y + left_y)

    # 왼쪽 개수가 더 적을 경우에 왼쪽을 전부 right와 매칭 시킨 후 1 추가한다.
    # 따라서 오른쪽은 left_x 만큼 개수를 줄여준다.
    if left_x < right_x:
        arr[right] = (right_y, right_x - left_x)
        left += 1
    # right가 더 적을 경우에는 반대로 하면 된다.
    elif left_x > right_x:
        arr[left] = (left_y, left_x - right_x)
        right -= 1
    # 개수가 동일하면 둘 다의 위치 모두를 옮겨준다.
    else:
        left += 1
        right -= 1

print(ans)