n, k, l = map(int, input().split())
# 공책 개수, 추가 포스트잇 최대 개수, 하나의 포스트잇에 적을 수 있는 공책 번호 개수
arr = list(map(int, input().split()))

def find(h):
    num = 0
    for i in range(n - h, n):
        if arr[i] < h:
            num += (h - arr[i])
    
    return num <= k * l and arr[n - h] + k >= h

arr.sort()

ans = 0
left = 0
right = n
while left <= right:
    mid = (left + right) // 2

    if find(mid):
        ans = max(ans, mid)
        left = mid + 1
    else:
        right = mid - 1

print(ans)