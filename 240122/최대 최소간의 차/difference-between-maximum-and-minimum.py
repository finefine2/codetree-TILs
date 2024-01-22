n, k = map(int, input().split())

arr = list(map(int, input().split()))


ans = 10000
for i in range(10000 - k + 1):
    num = 0
    for j in range(n):
        if arr[j] < i:
            num += abs(i - arr[j])
        elif arr[j] > i + k:
            num += abs(arr[j] - (i + k))

    ans = min(ans, num)


print(ans)









# # 0 부터 100 - 17 까지
# for i in range(83):
#     num = 0
#     for j in range(n):
#         if arr[j] < i:
#             num += (i - arr[j]) ** 2
#         elif arr[j] > i + 17:
#             num += (arr[j] - (i + 17)) * (arr[j] - (i + 17))
    
#     # i 부터 i + 17 이라고 가정
#     # i + 17 보다 높으면 i + k가 되게 깎고
#     # i보다 작으면 i가 되게 쌓는다.

#     ans = min(ans, num)