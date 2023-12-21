N = int(input()) 

mapper = {
    'W': 0, 
    'S': 1,
    'N': 2,
    'E': 3
}
drs = [0,1,-1,0]
dcs = [-1,0,0,1]

r,c = 0,0
t = 0 
ans = -1 
for _ in range(N): 
    d, s = input().split() 
    move_d = mapper[d] 

    for i in range(int(s)): 
        r += drs[move_d]
        c += dcs[move_d] 
        t += 1
        if r == 0 and c == 0:
            ans = t
            break 
print(ans)