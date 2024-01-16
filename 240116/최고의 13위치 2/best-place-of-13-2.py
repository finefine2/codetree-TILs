n = int(input())

arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


Max = -1
for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i == k and abs(j - l) < 3:
                    continue
                
                a = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                b = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                if Max < (a + b):
                    Max = a + b

print(Max)