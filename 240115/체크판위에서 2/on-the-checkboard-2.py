n, m = map(int, input().split())

arr = []
for _ in range(n):
    tmp = list(map(str, input().split()))
    arr.append(tmp)



# 점프 진행시 현재 위치와 이후의 색이 달라야 함
# 점프 진행시 적어도 한칸 오른쪽으로 가야 하며 동시에 한칸 이상 아래로 가야함
# 시작 도착을 제외하고 점프로 도달한 위치가 정확히 2곳 이어야 한다.


ans = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i+1, n-1):
            for l in range(j+1, m-1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[k][l] and arr[k][l] != arr[n-1][m-1]:
                    ans += 1

print(ans)