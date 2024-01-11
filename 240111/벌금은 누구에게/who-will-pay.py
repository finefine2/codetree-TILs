n, m, k = map(int, input().split())

arr = [0] * (n+1)
arr2 = []
for i in range(m):
    a = int(input())

    arr[a] += 1
    if arr[a] >= k:
        arr2.append(a)
        break

print(arr2[0])