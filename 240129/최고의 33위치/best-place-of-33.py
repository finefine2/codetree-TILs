n = int(input())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)


Max = -1
for i in range(n-2):
    for j in range(n-2):
        cnt = 0
        for k in range(3):
            for l in range(3):
                if arr[i+k][j+l] == 1:
                    cnt += 1
        if cnt > Max:
            Max = cnt

print(Max)