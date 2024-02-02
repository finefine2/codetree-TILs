n, m, k = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


for i in range(n):
    check = False
    for j in range(k-1, k+m-1):
        if arr[i][j] != 0:
            check = True
    
    if not check:
        if i != 0:
            for j in range(k-1, k+m-1):
                arr[i-1][j] = 0
                arr[i][j] = 1
        else:
            for j in range(k-1, k+m-1):
                arr[i][j] = 1
    else:
        break


    # for j in range(k-1, k+m-1):
    #     if arr[i][j] == 0:
    #         arr[i][j] = 1
    #         cnt += 1

    # if cnt == m and i != 0:
    #     for l in range(k-1, n):
    #         arr[i-1][l] = 0 
    # elif cnt == m and i == 0:
    #     continue
    # else:
    #     for l in range(k-1, n):
    #         arr[i][l] = 0
    #     break

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()