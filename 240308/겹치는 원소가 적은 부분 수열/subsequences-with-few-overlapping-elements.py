n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = {}
left = 0
ans = 0

for right in range(n):
    count[arr[right]] = count.get(arr[right], 0) + 1
    # get은 arr[right]의 값을 출력해준다.
    # 뒤의 0은 arr[right]가 없을때에는 0을 출력해준다는 뜻이다.

    while count[arr[right]] > k:
        count[arr[left]] -= 1
        left += 1

    ans = max(ans, right - left + 1)


print(ans)