n = int(input())
arr = list(map(int, input().split()))

arr.sort()

idx = 1
num = arr[0]
ans = 0

while idx <= len(arr) - 1:
    ans += (num + arr[idx])
    num += arr[idx]
    idx += 1

print(ans)