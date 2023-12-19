# N E S W 
# 0 
dx = [0,1,0,-1]
dy = [1,0,-1,0]

dir_num = 0 
s = input()
x,y = 0,0
for s in s: 
    if s == "F":
        x, y = x + dx[dir_num], y + dy[dir_num]
    elif s == "L": 
        dir_num = (dir_num-1) % 4 
    elif s == "R": 
        dir_num = (dir_num+1) % 4 
print(x,y)