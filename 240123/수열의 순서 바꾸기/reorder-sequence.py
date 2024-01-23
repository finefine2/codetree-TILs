n = int(input())

arr = list(map(int, input().split()))

arr2 = arr
arr2.sort()

cnt = 0
for i in range(n-2, -1, -1):
    if arr[i] >= arr[i+1]:
        break
    cnt += 1

# print(cnt)
if arr == arr2:
    print(0)
else:
    print(n - cnt + 1)
# n - cnt - 1