n, m = map(int, input().split())

arr1 = []
arr2 = []
a, b = 0, 0
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 1+y):
        arr1.append(a + j * x)
    a += x*y

for i in range(m):
    x, y = map(int, input().split())
    for j in range(1, 1+y):
        arr2.append(b + j * x)
    b += x*y

one = False
cnt = 1
for i in range(max(len(arr1), len(arr2))):
    if i == 0:
        if arr1[i] >= arr2[i]:
            one = True
        else:
            one = False
    else:
        if arr1[i] >= arr2[i] and not one:
            cnt += 1
        elif arr1[i] < arr2[i] and one:
            cnt += 1

print(cnt)