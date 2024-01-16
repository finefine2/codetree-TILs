import sys
n = int(input())

def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

ans = sys.maxsize
for i in range(0,n-1):
    k = 0
    tmp = 0
    for j in range(1, n):
        if i == j:
            continue
        k += dist(arr[tmp][0], arr[tmp][1], arr[j][0], arr[j][1])
        tmp = j
    ans = min(ans, k)


print(ans)