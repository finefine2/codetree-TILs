n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

Max = -1
for i in range(n):
    for j in range(m-2):
        s = 0
        for k in range(3):
            s += arr[i][j+k]
        if s > Max:
            Max = s

for i in range(m):
    for j in range(n-2):
        s = 0
        for k in range(3):
            s += arr[j+k][i]
        if s > Max:
            Max = s

# --
# |
for i in range(n-1):
    for j in range(m-1):
        s = 0
        s += arr[i][j] + arr[i+1][j] + arr[i][j+1]
        
        if s > Max:
            Max = s
# --
#  |
for i in range(n-1):
    for j in range(m-1):
        s = 0
        s += arr[i][j] + arr[i+1][j] + arr[i+1][j+1]
        
        if s > Max:
            Max = s

# |
# --
for i in range(n-1):
    for j in range(m-1):
        s = 0
        s += arr[i][j] + arr[i+1][j+1] + arr[i][j+1]
        
        if s > Max:
            Max = s
#  |
# --
for i in range(n-1):
    for j in range(m-1):
        s = 0
        s += arr[i+1][j+1] + arr[i+1][j] + arr[i][j+1]
        
        if s > Max:
            Max = s



print(Max)