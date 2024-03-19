n, m, c = map(int, input().split())
# 사람, 버스, 최대 인원
arr = list(map(int, input().split()))

arr.sort()

def check(t):
    bus = 1
    first_t = arr[0]
    first_idx = 0

    for i in range(n):
        # 시간을 넘었거나 c명을 다 채운 경우 출발하고 세로운 버스 가져온다.
        # t를 무조건 그 안에 해결하는 것으로 가정하고 찾아보는 것이다.
        if arr[i] - first_t > t or i + 1 - first_idx > c:
            bus += 1
            first_t = arr[i]
            first_idx = i

    return bus <= m


left = 0
right = 1000000000
ans = 1000000000

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        ans = min(ans, mid)
        right = mid - 1
    else:
        left = mid + 1

print(ans)