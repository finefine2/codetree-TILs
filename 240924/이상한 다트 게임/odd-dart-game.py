from collections import deque
def in_range(r,c):
    return 0<=r<N and 0<=c<M

def bfs(sr,sc):
    # 두 개 이상 인접한 같은 값일 경우 v[]에 표시
    q = deque()

    q.append((sr,sc))
    v[sr][sc]=1             # 한 개 였다면 0으로 바꾸고 리턴해야함
    cnt=1
    drs,dcs = [1,0,-1,0],[0,1,0,-1]
    while q:
        ci,cj=q.popleft()
        # 네방향(j연산후 %M), 범위내, 미방문, 값이 같으면
        for dr,dc in zip(drs,dcs):
            nr,nc = ci+dr, (cj+dc) % M
            if in_range(nr,nc) and v[nr][nc] == 0 and arr[nr][nc] == arr[ci][cj]:
                q.append((nr,nc))
                v[nr][nc] = 1
                cnt += 1
    # 인접한 같은값 없는것이므로.. 원상복구!
    if cnt == 1:
        v[si][sj] = 0
N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x,d,k = map(int, input().split())
    # [1] x의 배수자리(x-1부터) di방향(0==시계방향), K칸 회전
    # x의 배수자리 회전
    for i in range(x-1,N,x):
    # 시계방향
        if d == 0:
            arr[i] = arr[i][:-k] + arr[i][-k:]
    # 반시계방향
        else:
            arr[i] = arr[i][:k] + arr[i][k:]

    # [2] 인접하면서 같은숫자를 표시(v[])
    v = [[0] * M for _ in range(N)]
    # 전체를 순회하면서 미방문, >0값이면 연결방문(같은값)
    for r in range(N):
        for c in range(M):
            if v[r][c] == 0 and arr[r][c] > 0:
                bfs(r,c)
    # (i,j)와 같은, 인접한 값 모두 표시

    # [2-1] v[]에 표시된 숫자 있는 경우 모두 지움
    def_flag,sm,cnt = 0,0,0
    for r in range(N):
        for c in range(M):
            if v[r][c] == 1: # 인접한 같은 값 표시
                arr[r][c] = 0
                del_flag = 1
            else: # 표시 안된 값
                if arr[r][c] > 0:
                    sm += arr[r][c]  #avg를 구하기 위해
                    cnt += 1


    # [2-2] 없는 경우: 평균구해서 크면 -1, 작으면 +1
    # 나눗셈 분모에 있는값은 조건추가!
    if del_flag == 0 and cnt > 0:
        avg = sm / cnt
        for r in range(N):
            for c in range(M):
                if avg < arr[r][c]:
                    arr[r][c] -= 1
                elif 0 < arr[r][c] < avg:
                    arr[r][c] += 1

    # 가지치기: 모두 0인경우 더이상 진행X
    if sm == 0:
        break
print(sum(map(sum,arr)))