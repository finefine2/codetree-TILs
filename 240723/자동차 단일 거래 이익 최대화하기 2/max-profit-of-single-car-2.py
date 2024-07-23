n = int(input())
arr = list(map(int, input().split()))

ans = -1
num = arr[0]
flag = False
for i in range(1, len(arr)-1):
    if num > arr[i]:
        num = arr[i]
        flag = True
    if arr[i+1] - num >= 0:
        ans = max(ans, arr[i+1] - num)

print(ans)