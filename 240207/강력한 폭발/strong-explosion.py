n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

check = [[0] * n for _ in range(n)]

ans = 0
one = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            one.append((i, j))
            # 폭탄의 위치를 배열에 넣어준다.

def isin(a, b):
    return 0<=a<n and 0<=b<n

def bomb(x, y, num):
    explode = [[], [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]], [[-1, 0], [1, 0], [0,0], [0,-1], [0,1]],
    [[-1, -1], [-1, 1], [0,0], [1, -1], [1, 1]]]
    # 폭탄의 방향들을 정해준다.

    for i in range(5):
        dx, dy = explode[num][i]
        nx = x + dx
        ny = y + dy
        if isin(nx, ny):
            check[nx][ny] = 1
    
    # 방향들에 대해서 x에 더해주고 안에 있다면 check에 1을 표시해준다.

def count_bomb():
    
    for i in range(n):
        for j in range(n):
            check[i][j] = False
    # 폭탄 터진 뒤 배열을 초기화 한다.
    
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                bomb(i, j, arr[i][j])
    # arr가 있을 경우 즉 폭탄이 있을 경우 터지는 함수를 진행한다.
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j]:
                cnt += 1

    # 그러고 check에서 1의 개수를 세주고 리턴한다.
    
    return cnt

def find_area(cnt):
    global ans

    if cnt == len(one):
        ans = max(ans, count_bomb())
        return
    # 만약 cnt가 폭탄의 길이만큼 되면 그때 폭탄의 개수를 세서 최대와 비교해서 갱신한다.
    
    for i in range(1, 4):
        x, y = one[cnt]

        arr[x][y] = i
        find_area(cnt + 1)
        arr[x][y] = 0

    # 폭탄의 좌표에 대하여 arr에 각 번호를 넣어서 계속 들어가면서 진행해준다.


find_area(0)

print(ans)