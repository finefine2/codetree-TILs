n, m = map(int, input().split())

a = 0
arr1 = []
for i in range(n):
    x, y = map(str, input().split())
    if x == 'L':
        for j in range(a-1, a-int(y)-1, -1):
            arr1.append(j)
        a -= int(y)
    elif x == 'R':
        for j in range(a+1, a+int(y)+1):
            arr1.append(j)
        a += int(y)


b = 0
arr2 = []
for i in range(m):
    x, y = map(str, input().split())
    if x == 'L':
        for j in range(b-1, b-int(y)-1, -1):
            arr2.append(j)
        b -= int(y)
    elif x == 'R':
        for j in range(b+1, b+int(y)+1):
            arr2.append(j)
        b += int(y)

ans = -1
for i in range(len(arr1)):
    if arr1[i] == arr2[i]:
        ans = i+1
        break

print(ans)