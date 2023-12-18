N,M = map(int,input().split()) 

MAX_R = 1000 * 1000

vel_A = [] 
for _ in range(N): 
    v,t = map(int,input().split()) 
    # total += t
    for _ in range(t): 
        vel_A.append(v) 

vel_B = []
for _ in range(M): 
    v,t = map(int,input().split())
    for _ in range(t): 
        vel_B.append(v) 
pos_A = [0] * (len(vel_A) + 1)
pos_B = [0] * (len(vel_B) + 1)

cnt = [] 
for i in range(len(pos_A)-1): 
    pos_A[i] = pos_A[i-1] + vel_A[i] 
    pos_B[i] = pos_B[i-1] + vel_B[i] 
    cnt.append(pos_A[i] - pos_B[i])

ans = 0     

# print(pos_A)
# print(pos_B)
# print(cnt)
for i in range(len(cnt)-1): 
    if cnt[i] == 0 and cnt[i] != cnt[i+1]: 
        ans += 1 
    elif cnt[i] * cnt[i+1] < 0: 
        ans += 1
print(ans)