# my solution
# N = int(input()) 

# mapper = {
#     'W': 0, 
#     'S': 1,
#     'N': 2,
#     'E': 3
# }
# drs = [0,1,-1,0]
# dcs = [-1,0,0,1]

# r,c = 0,0
# t = 0
# flag = False
# ans = -1 
# for _ in range(N): 
#     d, s = input().split() 
#     move_d = mapper[d] 

#     for i in range(int(s)): 
#         r = r + drs[move_d]
#         c = c + dcs[move_d] 
#         t += 1
        
#         if r == 0 and c == 0:
#             flag = True 
#             ans = t
#             break 
#     if flag: 
#         break 
# print(ans) 

# given solution 
N = int(input()) 

r,c = 0,0 
# E W S N 
drs, dcs = [1,-1,0,0], [0,0,-1,1] 

ans = -1 
passed_time = 0 
# dir 방향으로 dist만큼 이동하는 함수 
# 0,0 에 도달하면 true를 return 
def move(move_dir, dist): 
    global r,c 
    global ans, passed_time
    for _ in range(dist): 
        r,c = r + drs[move_dir], c + dcs[move_dir] 
        passed_time += 1 
        # 0,0 으로 돌아오면 답을 갱신 
        if r == 0 and c == 0: 
            ans = passed_time
            return True
    return False 

for _ in range(N): 
    c_dir, dist = input().split()
    dist = int(dist) 
    if c_dir == "E": 
        move_dir = 0
    elif c_dir == "W": 
        move_dir = 1 
    elif c_dir == "S": 
        move_dir = 2 
    else: 
        move_dir = 3 
    # 주어진 방향대로 dist만큼 이동 
    done = move(move_dir, dist) 
    if done: 
        break 
print(ans)