n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

total = 0
for i in range(n-1):
    total += distance(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])

result = float("inf")
for i in range(1, n-1): #하나를 건너뛰는 포인트
    check = total - distance(arr[i-1][0], arr[i-1][1], arr[i][0], arr[i][1])\
    - distance(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])\
    + distance(arr[i-1][0], arr[i-1][1], arr[i+1][0], arr[i+1][1])
    result = min(result, check)
print(result)