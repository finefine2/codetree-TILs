def bfs(si,sj):
    # 두 개 이상 인접한 같은 값일 경우 v[]에 표시
    q = []

    q.append((si,sj))
    v[si][sj]=1             # 한 개 였다면 0으로 바꾸고 리턴해야함
    cnt=1

    while q:
        ci,cj=q.pop(0)
        # 네방향(j연산후 %M), 범위내, 미방문, 값이 같으면
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj=ci+di, (cj+dj)%M
            if 0<=ni<N and v[ni][nj]==0 and arr[ci][cj]==arr[ni][nj]:
                q.append((ni,nj))
                v[ni][nj]=1
                cnt+=1

    if cnt==1:              # 인접한 같은값 없는것이므로.. 원상복구!
        v[si][sj]=0

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(T):
    x,d,k = map(int, input().split())
    # [1] x의 배수자리(x-1부터) di방향(0==시계방향), K칸 회전
    for i in range(x-1,N,x):        # x의 배수자리 회전
        if d==0:                    # 시계방향
            arr[i]=arr[i][-k:]+arr[i][:-k]
        else:                       # 반시계방향
            arr[i]=arr[i][k:]+arr[i][:k]

    # [2] 인접하면서 같은숫자를 표시(v[])
    v = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):  # 전체를 순회하면서 미방문, >0값이면 연결방문(같은값)
            if v[i][j]==0 and arr[i][j]>0:
                bfs(i,j)    # (i,j)와 같은, 인접한 값 모두 표시

    # [2-1] v[]에 표시된 숫자 있는 경우 모두 지움
    del_flag,sm,cnt=0,0,0
    for i in range(N):
        for j in range(M):
            if v[i][j]==1:  # 인접한 같은값 표시
                arr[i][j]=0
                del_flag=1
            else:           # 표시 안된 값
                if arr[i][j]>0:
                    sm+=arr[i][j]   # avg를 구하기 위한 덧샘
                    cnt+=1

    # [2-2] 없는 경우: 평균구해서 크면 -1, 작으면 +1
    if del_flag==0 and cnt>0:
        avg = sm/cnt        # 나눗셈 분모에 있는값은 조건추가!
        for i in range(N):
            for j in range(M):
                if avg<arr[i][j]:
                    arr[i][j]-=1
                elif 0<arr[i][j]<avg:
                    arr[i][j]+=1

    if sm==0:               # 가지치기: 모두 0인경우 더이상 진행X
        break

print(sum(map(sum,arr)))