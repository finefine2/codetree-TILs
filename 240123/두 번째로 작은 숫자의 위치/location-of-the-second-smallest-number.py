n = int(input())

arr = list(map(int, input().split()))

arr2 = []
for k in arr:
    arr2.append(k)

arr2.sort()
num = arr2[0]
for i in range(len(arr2)):
    if num != arr2[i]:
        num = arr2[i]
        break
idx = 0
for i in range(len(arr)):
    if num == arr[i]:
        idx = i
        break

if arr.count(num) != 1:
    print(-1)
else:
    print(idx+1)