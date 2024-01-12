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
same = False
cnt = 1
for i in range(max(len(arr1), len(arr2))):
    if i == 0:
        if arr1[i] > arr2[i]:
            one = True
            same = False
        elif arr1[i] == arr2[i]:
            one = False
            same = True
        else:
            one = False
            same = False
    else:
        if arr1[i] > arr2[i] and not one:
            cnt += 1
            one = True
            same = False
        elif arr1[i] < arr2[i] and one:
            cnt += 1
            one = False
            same = False
        elif arr1[i] == arr2[i] and not same:
            cnt += 1
            one = False
            same = True
        if arr1[i] != arr2[i] and same:
            cnt += 1
            if arr1[i] > arr2[i]:
                one = True
            elif arr1[i] < arr2[i]:
                two = True
            same = False

print(cnt)