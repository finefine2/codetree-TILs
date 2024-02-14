import sys
n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

def find_Max():
    dpMax = [[101] * n for _ in range(n)]

    dpMax[0][0] = arr[0][0]

    for i in range(1, n):
        dpMax[i][0] = max(dpMax[i-1][0], arr[i][0])

    # 첫 번째 행 초기화
    for j in range(1, n):
        dpMax[0][j] = max(dpMax[0][j-1], arr[0][j])


    # 최대값을 최소로 만들기
    # 최소값을 최대로 만들기
    for i in range(1, n):
        for j in range(1, n):
            dpMax[i][j] = max(min(dpMax[i-1][j], dpMax[i][j-1]), arr[i][j])

    return dpMax[n-1][n-1]

# Maxsize = sys.maxsize
ans = 101
for k in range(1, 101):
    for i in range(n):
        for j in range(n):
            if arr[i][j] < k:
                arr[i][j] = 101

    Max = find_Max()
    if Max < 101:
        ans = min(ans, abs(Max - k))
        # k가 여기에서 lower_bound 역할을 한다.
        # 그때 그때 path에 따라서 low와 high가 달라지므로 두개의 배열로 나누어서 하면 안된다.
        # -> 다른 패스가 겹칠 수 있어서
        # print(k)

print(ans)


# for i in range(n):
#     for j in range(n):
#         print(dpMax[i][j], end = " ")
#     print()

# print()

# for i in range(n):
#     for j in range(n):
#         print(dpMin[i][j], end = " ")
#     print()