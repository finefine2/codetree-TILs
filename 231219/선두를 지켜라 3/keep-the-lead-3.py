N,M = map(int,input().split()) 
MAX_R = 1000000

pos_A = [0] * (1+MAX_R)
time_A = 1 
for _ in range(N): 
    v,t = map(int,input().split())
    for _ in range(t): 
        pos_A[time_A] = pos_A[time_A-1] + v 
        time_A += 1

pos_B = [0] * (1+MAX_R)
time_B = 1 
for _ in range(M): 
    v,t = map(int,input().split()) 
    for _ in range(t): 
        pos_B[time_B] = pos_B[time_B-1] + v 
        time_B += 1 

lead, ans = 0,0 
for i in range(1,time_A): 
    if pos_A[i] > pos_B[i]: 
        if lead == 2 or lead == 3: 
            ans += 1 
        lead = 1 
    elif pos_A[i] < pos_B[i]: 
        if lead == 1 or lead == 3: 
            ans += 1 
        lead = 2 
    elif pos_A[i] == pos_B[i]: 
        if lead == 1 or lead == 2: 
            ans += 1 
        lead = 3
print(ans+1)
'''
B 
A B 
A 
A B 
B
'''