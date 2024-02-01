arr = []
for i in range(4):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

st = input()

if st == "R":
    for i in range(4):
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


for i in range(4):
    for j in range(4):
        print(arr[i][j], end = " ")
    print()