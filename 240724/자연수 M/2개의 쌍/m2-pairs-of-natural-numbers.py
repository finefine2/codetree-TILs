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

# 이분탐색과 같이 arr를 sort한 뒤에 left, right를 통해서 제일 큰 값과 제일 작은 값부터 가운데까지 온다.

# 각각의 개수에 따라서 진행하는 데 만약에 right의 개수가 더 많을 경우에는 right에서 그 당시의 left수만큼을 빼주고, left는 옮긴다. left의 경우도 마찬가지다

# 이 과정을 진행하고 나서의 right_y와 left_y의 합을 구하면서 최대값을 구해주면 시간복잡도에 알맞게 구할 수 있다.

# 정렬하는데 O(NlogN), 매칭하는데 O(N)