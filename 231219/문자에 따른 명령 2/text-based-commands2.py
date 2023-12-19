dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0 
x,y = 0,0
s = input() 
s_list = [] 
for i in range(len(s)): 
    s_list.append(s[i])
nx, ny = 0,0 
for s in s_list: 
    if s == "L": 
        dir_num = (dir_num - 1) % 4 
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
    elif s == "R": 
        dir_num = (dir_num + 1) % 4 
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
    elif s == "F": 
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        
print(nx, ny)