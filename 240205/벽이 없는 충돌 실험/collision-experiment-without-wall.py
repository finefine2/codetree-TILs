t = int(input())

dir = {'U':0, 'D':1, 'L':2, 'R':3}
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

n, m = 0, 0
def isin(x, y):
    return 0<=x<4001 and 0<=y<4001

arr_index = [[-1 for _ in range(4001)] for _ in range(4001)]

for _ in range(t):
    n = int(input())

    arr = []
    for num in range(n):
        x, y, w, d = tuple(input().split())
        i, j, w, d = (-int(y)) * 2 + 2000, int(x) * 2 + 2000, int(w), dir[d]
        arr.append((num, i, j, w, d))
    
    t = -1

    for time in range(1, 4001):
        next_arr = []
        # 여기에 다음 시간에 존재할 구슬의 정보 잠깐 저장
        for k in arr:
            num, i, j, w, d = k
            nx, ny = i + dx[d], j + dy[d]
            if isin(nx, ny):
                if arr_index[nx][ny] == -1:
                    next_arr.append((num, nx, ny, w, d))
                    # 이동할 위치가 안이고 다음으로 움직일때 그 위치가 아직 다른 구슬이 없다면 넣는다.
                    arr_index[nx][ny] = len(next_arr) - 1
                    # arr_index에는 next_arr의 크기보다 1작게 해서 넣는다. 있음을 표시
                else:
                    t = time

                    # 무게가 더 클 경우, 현재 구슬이 그 위치를 차지하고, 원래 위치의 구슬은 제거
                    if next_arr[arr_index[nx][ny]][3] < w:
                        next_arr[arr_index[nx][ny]] = (num, nx, ny, w, d)
                    # 원래 있던 구슬의 무게는 같지만, 이동하려는 구슬의 번호보다 작은 경우 갱신한다.
                    elif next_arr[arr_index[nx][ny]][3] == w and next_arr[arr_index[nx][ny]][0] < num:
                        next_arr[arr_index[nx][ny]] = (num, nx, ny, w, d)
        
        arr = next_arr[:]
        for k in next_arr:
            arr_index[k[1]][k[2]] = -1
        # next_arr을 arr에 넣어주고 arr_index를 매번 초기화 해주는 것
    
    print(t)