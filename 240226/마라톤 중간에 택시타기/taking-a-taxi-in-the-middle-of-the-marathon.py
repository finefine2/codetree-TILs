# n = int(input())

# def get_dist(x1, y1, x2, y2):
#     return abs(x1 - x2) + abs(y1 - y2)

# arr = []
# for i in range(n):
#     x, y = map(int, input().split())
#     arr.append((x, y))

# L = [0] * (n+1)
# R = [0] * (n+1)

# for i in range(n-1):
#     L[i+1] = L[i] + get_dist(arr[i][0], arr[i+1][0], arr[i][1], arr[i+1][1])

# for i in range(n-2, -1, -1):
#     R[i+1] = R[i] + get_dist(arr[i][0], arr[i+1][0], arr[i][1], arr[i+1][1])

# import sys
# ans = sys.maxsize
# for i in range(1, n-2):
#     k = L[i - 1] + R[i + 1] + get_dist(arr[i][0], arr[i+1][0], arr[i][1], arr[i+1][1])
#     ans = min(ans, k)


# print(ans)

n = int(input())

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

total_dist = 0
for i in range(n-1):
    total_dist += get_dist(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])
# 전체 거리를 구해준다.

max_save = 0
for i in range(1, n-1):
    skip_dist = get_dist(arr[i-1][0], arr[i-1][1], arr[i+1][0], arr[i+1][1])
    current_dist = get_dist(arr[i-1][0], arr[i-1][1], arr[i][0], arr[i][1]) + get_dist(arr[i][0], arr[i][1], arr[i+1][0], arr[i+1][1])
    save = current_dist - skip_dist
    max_save = max(max_save, save)
# 중간의 거리를 뺀 것들 중에 max 구하기

# 전체 거리에서 빼려는 거리 빼서 출력
print(total_dist - max_save)