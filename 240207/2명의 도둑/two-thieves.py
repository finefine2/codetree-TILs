n, m, c = map(int, input().split())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

value = [[-1] * n for _ in range(n)]

tmp = []
Max = 0

def find_sum(now, weight, now_value):
    global Max

    if now == m:
        if weight <= c:
            Max = max(Max, now_value)
        return
    # 선택한 크기가 m이 될 경우 리턴해준다.
    
    find_sum(now + 1, weight, now_value)
    find_sum(now + 1, weight + tmp[now], now_value + tmp[now] * tmp[now])
    # now_value일때랑 weight와 now_value일 때 더해주면서 두 방향으로 들어가기


def find_max(x, y):
    global tmp, Max

    if value[x][y] != -1:
        return value[x][y]
    
    # arr에서 x 고정, y는 m개의 영역에
    tmp = arr[x][y:y+m]
    Max = 0
    find_sum(0,0,0)
    # 0,0,0 으로 시작해준다.

    value[x][y] = Max

    return Max

def inter(a, b, c, d):
    return not (b < c or d < a)

def ok(x1, y1, x2, y2):
    if y1 + m - 1 >= n or y2 + m - 1 >= n:
        return False
    # 범위가 넘으면 False
    
    if x1 != x2:
        return True
    # x값 다르면 True
    
    if inter(y1, y1 + m - 1, y2, y2 + m - 1):
        return False
    # 교차할 경우 False

    return True

ans = 0  

for x1 in range(n):
    for y1 in range(n):
        for x2 in range(n):
            for y2 in range(n):
                if ok(x1, y1, x2, y2):
                    # 모든 좌표에 대해서 ok이면 x1,y1의 Max와 x2,y2의 Max를 더해준다.
                    current_sum = find_max(x1, y1) + find_max(x2, y2)

                    if current_sum > ans:
                        ans = current_sum
                    # 최대값보다 크면 갱신한다.

print(ans)