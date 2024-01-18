n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

check = False
for i in range(11):
    for j in range(11):
        for k in range(11):
            flag = 0
            for l in range(len(arr)):
                if arr[l][0] == i or arr[l][1] == i or arr[l][0] == j or arr[l][1] == j or arr[l][0] == k or arr[l][1] == k:
                    flag = 2
                else:
                    flag = 3
            if flag == 2:
                check = True

if check:
    print(1)
else:
    print(0)