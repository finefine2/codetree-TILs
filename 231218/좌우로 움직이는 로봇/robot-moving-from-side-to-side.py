N,M = map(int,input().split()) 
MAX_R = 50000
pos_A = [0] * (MAX_R+1)
pos_B = [0] * (MAX_R+1)

time_a = 1
time_b = 1

# A가 있는 위치를 기록 
for _ in range(N): 
    t,d = input().split()
    t = int(t)
    if d == "L": 
        for _ in range(t): 
            pos_A[time_a] = pos_A[time_a-1] - 1 
            time_a += 1 
    elif d == "R": 
        for _ in range(t): 
            pos_A[time_a] = pos_A[time_a-1] + 1 
            time_a += 1 
    
# B가 있는 위치를 기록 
for _ in range(M): 
    t,d = input().split()
    t = int(t) 
    if d == "L": 
        for _ in range(t): 
            pos_B[time_b] = pos_B[time_b-1] - 1
            time_b += 1 
    elif d == "R": 
        for _ in range(t): 
            pos_B[time_b] = pos_B[time_b-1] + 1 
            time_b += 1 

if time_a < time_b: 
    for i in range(time_a, time_b): 
        pos_A[i] = pos_A[i-1] 
elif time_a > time_b: 
    for i in range(time_b, time_a): 
        pos_B[i] = pos_B[i-1]
cnt = 0 
t_max = max(time_a, time_b) 

for i in range(1,t_max): 
    if pos_A[i-1] != pos_B[i-1] and pos_A[i] == pos_B[i]: 

        cnt += 1
print(cnt)