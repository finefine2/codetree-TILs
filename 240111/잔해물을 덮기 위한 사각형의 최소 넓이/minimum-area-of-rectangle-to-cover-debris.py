arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr = [[0] * 3030 for _ in range(3030)]

cnt = 0
for i in range(arr1[0], arr1[2]):
    for j in range(arr1[1], arr1[3]):
        arr[i+1000][j+1000] = 1
        

for i in range(arr2[0], arr2[2]):
    for j in range(arr2[1], arr2[3]):
        arr[i+1000][j+1000] = -1
        

Minx = 3000
Miny = 3000
Maxx = -1000
Maxy = -1000
for i in range(3020):
    for j in range(3020):
        if arr[i][j] == 1:
            if i <= Minx and j <= Miny:
                Minx = i 
                Miny = j 
                # print(Minx, Miny)
            if i >= Maxx and j >= Maxy:
                Maxx = i
                Maxy = j
                # print(Maxx, Maxy)

# print(Maxx, Maxy, Minx, Miny)
print((Maxx - Minx + 1) * (Maxy - Miny + 1))