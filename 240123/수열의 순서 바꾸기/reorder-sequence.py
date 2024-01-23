n = int(input())

arr = list(map(int, input().split()))

arr2 = arr
arr2.sort()

cnt = 0
for i in range(n-2, 0, -1):
    if arr[i] >= arr[i+1]:
        break
    cnt += 1

print(n - cnt + 1)