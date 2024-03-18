n, m = map(int, input().split())

Max = 0
arr = []
for i in range(m):
    a, b = map(int, input().split())
    arr.append((a, b))
    Max = max(Max, b)

arr.sort()
ans = 0

left = 1
right = Max

def find(dist):
    cnt = 1
    point = arr[0][0]

    for start, end in arr:
        if point + dist > end:
            continue
        
        if point + dist < start:
            point = start
            cnt += 1
        
        dot = max((end - point) // dist, 0)
        cnt += dot
        point += dot * dist
    
    return cnt >= n



while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)