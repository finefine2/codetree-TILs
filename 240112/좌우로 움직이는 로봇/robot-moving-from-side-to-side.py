n, m = map(int, input().split())

arr1 = []
arr2 = []

a = 0
for i in range(n):
    x, y = map(str, input().split())
    x = int(x)
    if y == 'L':
        for j in range(1,x+1):
            arr1.append(a - j)
        a -= x
    else:
        for j in range(1,x+1):
            arr1.append(a + j)
        a += x
b = 0
for i in range(m):
    x, y = map(str, input().split())
    x = int(x)
    if y == 'L':
        for j in range(1,x+1):
            arr2.append(b - j)
        b -= x
    else:
        for j in range(1,x+1):
            arr2.append(b + j)
        b += x
cnt = 0

for i in range(1, max(len(arr2), len(arr1))):
    if i >= len(arr1):
        k = arr1[len(arr1) - 1]
        if k == arr2[i]:
            cnt += 1
    elif i >= len(arr2):
        k = arr2[len(arr2) - 1]
        if k == arr1[i]:
            cnt += 1
    elif arr1[i] == arr2[i] and arr1[i-1] != arr2[i-1]:
        cnt += 1
    

print(cnt)

# for k in arr1:
#     print(k, end = " ")
# print()
# for k in arr2:
#     print(k, end= " ")