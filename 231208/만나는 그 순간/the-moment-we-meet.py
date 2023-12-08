MAX_T = 100000

n,m = map(int,input().split()) 
pos_a, pos_b = [0] * (1+MAX_T), [0] * (1+MAX_T) 

# A 가 매 초마다 서있는 위치 기록
time_a = 1
for _ in range(n): 
    d,t = input().split() 
    for _ in range(int(t)): 
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1 
# B 가 매 초마다 서있는 위치 기록
time_b = 1 
for _ in range(m): 
    d,t = input().split() 
    for _ in range(int(t)): 
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

# 최초로 만난다 
ans = -1 
for i in range(1, time_a): 
    if pos_a[i] == pos_b[i]: 
        ans = i 
        break 
print(ans)