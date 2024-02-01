N = int(input()) 
fights = [list(map(int,input().split())) for _ in range(N)] 

ans = 0 
win = 0 
# 1 > 2 > 3 
for a,b in fights: 
    if a == 1 and b == 2: 
        win += 1 
    elif a == 2 and b == 3: 
        win += 1 
    elif a == 3 and b == 1: 
        win += 1 
ans = max(ans,win) 

# 1 > 3 > 2 
win = 0 
for a,b in fights: 
    if a == 1 and b == 3: 
        win += 1 
    elif a == 3 and b == 2: 
        win += 1 
    elif a == 2 and b == 1: 
        win += 1 
ans = max(ans,win) 
print(ans)