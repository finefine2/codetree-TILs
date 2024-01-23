n = int(input())

arr = list(map(int, input().split()))

ans = 0
for i in range(n-2, -1, -1):
    if arr[i] > arr[i+1]:
        ans = i + 1
        break

print(ans)

# cnt = 0
# for i in range(n-2, -1, -1):
#     if arr[i] < arr[i+1]:
#         break
#     cnt += 1

# print(cnt)
# print(n - cnt + 1)
# n - cnt - 1

# num = 0
# now = n-2
# while now >= 0 and arr[now] < arr[now + 1] :
#     now -= 1
#     num += 1

# # print(num)
# print(now + 1)