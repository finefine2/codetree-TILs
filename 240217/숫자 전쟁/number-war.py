n = int(input())

arr1 = [0] + list(map(int, input().split()))
arr2 = [0] + list(map(int, input().split()))

# 자신이 상대방 보다 작을 경우 카드에 적혀있는 점수 얻고 카드 번호 작은 사람의 카드를 버린다.
# 같을 경우 두 명 모두 점수를 얻지 못하며 둘의 카드를 모두 버린다.

dp = [[-1] * (n+1) for _ in range(n+1)]

dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        
        if i < n and arr1[i+1] < arr2[j+1]:
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
        # 첫번째가 더 작을 경우에는 dp가 i+1로 간다.
        # 첫번째는 사실 알 필요가 없어서 더하지 않고 i+1로 넘어간다.

        if j < n and arr1[i+1] > arr2[j+1]:
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + arr2[j+1])
        # 두번째가 더 작은 경우에는 뒤에 arr2[j+1]을 추가한다.
        # 두번째 값을 구해야 하므로 arr2만 더해준다.

        # 같은 경우는 둘다 그냥 넘어간다.
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][n], dp[n][i])

print(ans)  



# left = 0
# right = 0
# a, b = 0, 0

# arr1.sort()
# arr2.sort()
# while left == n-1 or right == n-1:
#     if arr1[left] < arr2[right]:
#         a += arr1[left]
#         left += 1
#     elif arr1[left] < arr2[right]:
#         b += arr2[right]
#         right += 1
#     else:
#         left += 1
#         right += 1

# print(b)