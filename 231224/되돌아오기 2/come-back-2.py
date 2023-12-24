# my solution 
# s_in = input()
# r,c = 0,0

# drs = [0,1,0,-1]
# dcs = [1,0,-1,0]

# time = 0 
# dirs = 3 
# flag = False

# def turn(direction, c): 
#     if c == "L":
#         direction = (direction-1) % 4 
#     else: 
#         direction = (direction+1) % 4 
#     return direction

# for s in s_in: 
#     time += 1
#     if s == "F":
#         r += drs[dirs]
#         c += dcs[dirs]
#     else: 
#         dirs = turn(dirs,s)
#     if r == 0 and c == 0: 
#         flag = True 
#         break 
# if flag: 
#     print(time) 
# else:
#     print(-1)

# given solution 

dirs = input() 
r,c = 0,0
curr_dir = 3 

# E S W N 
drs = [0,1,0,-1]
dcs = [1,0,-1,0]

flag = False

for i in range(len(dirs)): 
    c_dir = dirs[i] 
    if c_dir == "L": 
        curr_dir = (curr_dir-1) % 4
    elif c_dir == "R": 
        curr_dir = (curr_dir+1) % 4 
    else: 
        r = r + drs[curr_dir]
        c = c + dcs[curr_dir]
    if r == 0 and c == 0: 
        print(i+1) 
        flag = True
        break 
if flag == False: 
    print(-1)