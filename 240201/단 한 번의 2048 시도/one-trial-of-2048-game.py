arr = []
for i in range(4):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

st = input()

if st == "R":
    for i in range(4):
        for j in range(2, 0, -1):
            if arr[i][j] == 0:
                for k in range(j, 0, -1):
                    arr[i][k] = arr[i][k-1]
                    arr[i][k-1] = 0
        check = False
        for j in range(2, 0, -1):
            if arr[i][j] == arr[i][j+1] and not check:
                arr[i][j+1] = arr[i][j] + arr[i][j+1]
                arr[i][j] = 0
                check = True
        for j in range(2, 0, -1):
            if arr[i][j] == 0:
                for k in range(j, 0, -1):
                    arr[i][k] = arr[i][k-1]
                    arr[i][k-1] = 0
elif st == "L":
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                for k in range(j,3):
                    arr[i][k] = arr[i][k+1]
                    arr[i][k+1] = 0
        check = False
        for j in range(3):
            if arr[i][j] == arr[i][j+1] and not check:
                arr[i][j] = arr[i][j] + arr[i][j+1]
                arr[i][j+1] = 0
                check = True
        for j in range(4):
            if arr[i][j] == 0:
                for k in range(j,3):
                    arr[i][k] = arr[i][k+1]
                    arr[i][k+1] = 0

if st == "D":
    for j in range(4):
        for i in range(2, 0, -1):
            if arr[i][j] == 0:
                for k in range(i, 0, -1):
                    arr[k][j] = arr[k-1][j]
                    arr[k-1][j] = 0
        check = False
        for i in range(3, 0, -1):
            if arr[i][j] == arr[i-1][j] and not check:
                arr[i][j] = arr[i][j] + arr[i-1][j]
                arr[i-1][j] = 0
                check = True
        for i in range(2, 0, -1):
            if arr[i][j] == 0:
                for k in range(i, 0, -1):
                    arr[k][j] = arr[k-1][j]
                    arr[k-1][j] = 0
elif st == "U":
    for j in range(4):
        for i in range(4):
            if arr[i][j] == 0:
                for k in range(i,3):
                    arr[k][j] = arr[k+1][j]
                    arr[k+1][j] = 0
        check = False
        for i in range(3):
            if arr[i][j] == arr[i+1][j] and not check:
                arr[i][j] = arr[i][j] + arr[i+1][j]
                arr[i+1][j] = 0
                check = True
        for i in range(4):
            if arr[i][j] == 0:
                for k in range(i,3):
                    arr[k][j] = arr[k+1][j]
                    arr[k+1][j] = 0


for i in range(4):
    for j in range(4):
        print(arr[i][j], end = " ")
    print()