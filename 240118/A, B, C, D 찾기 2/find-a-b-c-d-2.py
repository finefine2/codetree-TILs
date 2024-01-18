arr = list(map(int, input().split()))
arr.sort()
flag = False
for i in range(1, 41):
    for j in range(1, 41):
        for k in range(1, 41):
            for l in range(1, 41):
                if not flag:
                    arr2 = []
                    arr2.append(i)
                    arr2.append(j)
                    arr2.append(k)
                    arr2.append(l)
                    arr2.append(i+j)
                    arr2.append(i+k)
                    arr2.append(i+l)
                    arr2.append(j+k)
                    arr2.append(j+l)
                    arr2.append(k+l)
                    arr2.append(i+j+k)
                    arr2.append(i+j+l)
                    arr2.append(i+k+l)
                    arr2.append(j+k+l)
                    arr2.append(i+j+k+l)
                    arr2.sort()
                    if arr == arr2:
                        print(i, j, k, l)
                        flag = True
                        break