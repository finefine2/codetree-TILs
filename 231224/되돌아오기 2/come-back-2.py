s_in = input()
r,c = 0,0

drs = [0,1,0,-1]
dcs = [1,0,-1,0]

time = 0 
dirs = 3 
flag = False

def turn(direction, c): 
    if c == "L":
        direction = (direction-1) % 4 
    else: 
        direction = (direction+1) % 4 
    return direction

for s in s_in: 
    time += 1
    if s == "F":
        r += drs[dirs]
        c += dcs[dirs]
    else: 
        dirs = turn(dirs,s)
    if r == 0 and c == 0: 
        flag = True 
        break 
if flag: 
    print(time) 
else:
    print(-1)