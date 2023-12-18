# 개고생했지만 맞긴함 
# N,M = map(int,input().split()) 

# vel_A = [] 
# for _ in range(N): 
#     v,t = map(int,input().split()) 
#     # total += t
#     for _ in range(t): 
#         vel_A.append(v) 

# vel_B = []
# for _ in range(M): 
#     v,t = map(int,input().split())
#     for _ in range(t): 
#         vel_B.append(v) 
# pos_A = [0] * (len(vel_A) + 1)
# pos_B = [0] * (len(vel_B) + 1)

# cnt = [] 
# for i in range(len(pos_A)-1): 
#     pos_A[i] = pos_A[i-1] + vel_A[i] 
#     pos_B[i] = pos_B[i-1] + vel_B[i] 
#     cnt.append(pos_A[i] - pos_B[i])

# ans = 0     

# # print(pos_A)
# # print(pos_B)
# # print(cnt)
# for i in range(len(cnt)-1): 
#     if cnt[i] == 0 and cnt[i] != cnt[i+1]: 
#         ans += 1 
#     elif cnt[i] * cnt[i+1] < 0: 
#         ans += 1
# print(ans)

# given sol 
MAX_T = 1000000
N,M = map(int,input().split()) 
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1) 

# A가 매 초마다 서있는 위치 기록 
time_a = 1 
for _ in range(N): 
    v,t = map(int,input().split())
    for _ in range(t): 
        pos_a[time_a] = pos_a[time_a-1] + v 
        time_a += 1 
# A가 매 초마다 서있는 위치 기록 
time_b = 1 
for _ in range(M): 
    v,t = map(int,input().split()) 
    for _ in range(t): 
        pos_b[time_b] = pos_b[time_b-1] + v 
        time_b += 1 
# A 와 B 중 더 앞서 있는 경우를 체크 
# A가 앞서면1, 반대면 2 
lead, ans = 0,0 
for i in range(1,time_a): 
    if pos_a[i] > pos_b[i]: 
        # 기존 리더가 b면 갱신 
        if lead == 2: 
            ans += 1 
        # A가 리드로 변경 
        lead = 1 
    elif pos_a[i] < pos_b[i]: 
        # 기존 리더가 A면 갱신 
        if lead == 1: 
            ans += 1 
        # B 리드로 변경 
        lead = 2 
print(ans)