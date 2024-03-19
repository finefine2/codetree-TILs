a = input()
b = input()
arr = list(map(int, input().split()))

ans = -1
n = len(a)
m = len(b)
check = [0] * n

def find(mid):
    idx = 0

    for i in range(mid):
        check[arr[i] - 1] = 1
    
    for i in range(n):
        if check[i]:
            continue
        if idx < m and a[i] == b[idx]:
            idx += 1
        # 인덱스가 끝나지 않았는데 해당하는 단어가 있을 경우 idx를 늘려준다.

    return idx == m
    # idx가 m이 될 경우 끝

left = 0
right = n

while left <= right:
    mid = (left + right) // 2
    if find(mid):
        left = mid + 1
        ans = max(ans, mid)
    else:
        right = mid - 1
    
    for i in range(mid):
        check[arr[i] - 1] = 0
    # mid 까지의 check를 다시 초기화한다.

print(ans + 1)