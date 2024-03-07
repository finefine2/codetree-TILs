n, k = map(int, input().split())

arr = [0]
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

arr1 = [0] * (n+1)
arr2 = [0] * (n+1)

arr.sort()

s = 0
i = 1
for j in range(1, n+1):
    while i + 1 <= j and arr[j] - arr[i] > k:
        i += 1
    
    s = max(s, j - i + 1)

    arr1[j] = s

s = 0
j = n
for i in range(n, 0, -1):
    while j - 1 >= i and arr[j] - arr[i] > k:
        j -= 1
    
    s = max(s, j - i + 1)

    arr2[i] = s

ans = arr1[n]

for i in range(1, n):
    ans = max(ans, arr1[i] + arr2[i+1])

print(ans)