n, m, d, s = map(int, input().split())
# n명의 사람이 m개의 치즈
# 치즈 먹은 기록 : d
# 언제아팠는지 기록 : s

eat = []
for i in range(d):
    p, m, t = map(int, input().split())
    eat.append((p, m, t))
# p번째 사람이 m번째 치즈를 t초에 먹음

sick = []
for i in range(s):
    p, t = map(int, input().split())
    sick.append((p, t))
# p번째 사람이 t초에 아픔


ans = 0
for i in range(1, m+1):
    arr = [0] * (n+1)

    # 먹은거 탐색
    for k in eat:
        if k[1] != i:
            continue
        # 이 치즈가 아닌 경우 넘어간다.

        # 먹은 사람이 i번째에 처음 먹었거나 이전보다 더 빨리 먹을 경우 갱신
        user = k[0]
        if arr[user] == 0:       # 처음 먹은 경우 갱신
            arr[user] = k[2]
        elif arr[user] > k[2]:   # 처음 먹지 않고 더 빨리 먹은 경우
            arr[user] = k[2]     # 갱신 즉,, 제일 빠른 경우를 넣어주는 것

    check = True

    # 이때의 치즈를 먹지 않았거나 이때의 치즈를 먹은 시간 보다 먼저 아프면 False
    for k in sick:
        user = k[0]
        if arr[user] == 0:      # 이 당시의 시간에 먹지 않은 경우 False
            check = False
        if arr[user] >= k[1]:   # 먹은 시점이 더 클 경우에 관련없으므로 False
            check = False

    num = 0
    if check:
        for j in range(1, n+1):
            if arr[j] != 0:
                num += 1
        # arr에 있어서 이때의 치즈를 먹었으면 무조건이니까 num 증가
    ans = max(ans, num)   

print(ans)