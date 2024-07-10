n = int(input())

arr = [0] + list(map(int, input().split()))

Max = sum(arr)
dp = [0] * (Max + 1)
# arr 들의 합의 sum을 구해서 될 수 있는 곳까지 구한다.

# 처음인 0은 트루로 두고
# dp[j - arr[i]]가 true일때 dp[j]도 합을 만들 수 있으므로 true로 설정한다.
dp[0] = True
for i in range(n):
    for j in range(Max, 0, -1):
        if j - arr[i] >= 0 and dp[j - arr[i]]:
            dp[j] = True
# 중복이 되지 않고 한번씩만 쓸 수 있으므로 Max부터 0까지 뒤에서부터 한다.

ans = 100001
for i in range(1, Max):
    if dp[i]:
        ans = min(ans, abs(Max - 2 * i))
# 값이 Max - i, i 이기에 차이는 Max - 2 * i가 된다.

print(ans)




# n = int(input())

# arr = [0] + list(map(int, input().split()))

# Max = sum(arr)
# dp = [0] * (Max + 1)
# # 최대가 안주어졌으므로 sum으로 최대를 구해서 거기까지 잡기

# dp[0] = True
# for i in range(n):
#     for j in range(Max, 0, -1):
#         if j - arr[i] >= 0 and dp[j - arr[i]]:
#             dp[j] = True
#         # 원래의 조건인 j - arr[i]는 0 이상이어야 하고
#         # dp의 경우 j - arr[i]가 True일 경우에 그 다음것이 Tru로 이어진다.

# ans = 100001
# for i in range(1, Max):
#     if dp[i]:
#         ans = min(ans, abs(Max - 2 * i))
# # 여기에서 합이 Max - i 와 i로 나뉘므로 그 둘의 차는 Max - 2*i 이다.

# print(ans)
# # num = Max - sum(ans)
# # print(abs(sum(ans) - num))