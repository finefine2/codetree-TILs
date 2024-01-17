n, m, d, s = map(int, input().split())
# n명의 사람이 m개의 치즈
# 치즈 먹은 기록 : d
# 언제아팠는지 기록 : s

eat_records = [[] for _ in range(m + 1)]

for _ in range(d):
    p, cheese, t = map(int, input().split())
    eat_records[cheese].append((p, t))

# p번째 사람이 m번째 치즈를 t초에 먹음

sick = []
for _ in range(s):
    p, t = map(int, input().split())
    sick.append((p, t))
# p번째 사람이 t초에 아픔


ans = 0
for i in range(1, m+1):
    arr = [0] * (n+1)

    for eat_record in eat_records[i]:
        user, eat_time = eat_record
        if arr[user] == 0 or arr[user] > eat_time:
            arr[user] = eat_time

    # # 먹은거 탐색
    # for k in eat:
    #     if k[1] != i:
    #         continue
    #     # 이 치즈가 아닌 경우 넘어간다.

    #     # 먹은 사람이 i번째에 처음 먹었거나 이전보다 더 빨리 먹을 경우 갱신
    #     user = k[0]
    #     if arr[user] == 0 or arr[user] > k[2]:       
    #         arr[user] = k[2]
            
            # 처음 먹은 경우 갱신
            # 처음 먹지 않고 더 빨리 먹은 경우
            # 갱신 즉,, 제일 빠른 경우를 넣어주는 것

    check = True

    # 이때의 치즈를 먹지 않았거나 이때의 치즈를 먹은 시간 보다 먼저 아프면 False
    for k in sick:
        user = k[0]
        
        if arr[user] == 0 or arr[user] >= k[1]:     
            check = False
            # 이 당시의 시간에 먹지 않은 경우 False
           # 먹은 시점이 더 클 경우에 관련없으므로 False

    num = 0
    if check:
        for j in range(1, n+1):
            if arr[j] != 0:
                num += 1
        # arr에 있어서 이때의 치즈를 먹었으면 무조건이니까 num 증가
    ans = max(ans, num)   

print(ans)


# n, m, d, s = map(int, input().split())

# # 각 치즈에 대한 먹은 기록을 저장할 리스트 초기화
# eat_records = [[] for _ in range(m + 1)]

# for _ in range(d):
#     p, cheese, time = map(int, input().split())
#     eat_records[cheese].append((p, time))

# sick = []
# for _ in range(s):
#     p, time = map(int, input().split())
#     sick.append((p, time))

# ans = 0

# for i in range(1, m + 1):
#     arr = [0] * (n + 1)

#     # 치즈 i에 대한 먹은 기록을 확인
#     for eat_record in eat_records[i]:
#         user, eat_time = eat_record
#         if arr[user] == 0 or arr[user] > eat_time:
#             arr[user] = eat_time

#     check = True

#     # 아픈 기록 확인
#     for k in sick:
#         user = k[0]
#         if arr[user] == 0 or arr[user] >= k[1]:
#             check = False

#     num = 0
#     if check:
#         for j in range(1, n + 1):
#             if arr[j] != 0:
#                 num += 1
#     ans = max(ans, num)

# print(ans)