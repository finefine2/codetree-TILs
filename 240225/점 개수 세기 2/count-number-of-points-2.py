from sortedcontainers import SortedSet

n, q = map(int, input().split())

arr = SortedSet()
dic = dict()
num = 1

pre_sum = [[0] * 2002 for _ in range(2002)]

dot = []
for i in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))

rec = []
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    rec.append((x1, y1, x2, y2))

def get_lower_boundary(x):
    return arr.bisect_left(x) + 1

def get_upper_boundary(x):
    return arr.bisect_right(x)

def get_sum(x1, y1, x2, y2):
    return pre_sum[x2][y2] - pre_sum[x1 - 1][y2] - pre_sum[x2][y1 - 1] + pre_sum[x1 - 1][y1 - 1]


for x, y in dot:
    arr.add(x)
    arr.add(y)

num = 1
for k in arr:
    dic[k] = num
    num += 1

for x, y in dot:
    nx, ny = dic[x], dic[y]
    pre_sum[nx][ny] += 1

for i in range(1, num + 1):
    for j in range(1, num + 1):
        pre_sum[i][j] += pre_sum[i-1][j] + pre_sum[i][j-1] - pre_sum[i-1][j-1]

for x1, y1, x2, y2 in rec:
    nx1 = get_lower_boundary(x1)
    ny1 = get_lower_boundary(y1)
    nx2 = get_upper_boundary(x2)
    ny2 = get_upper_boundary(y2)

    ans = get_sum(nx1, ny1, nx2, ny2)
    
    print(ans)