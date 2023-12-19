N = int(input()) 
dr = [1,0,-1,0]
dc = [0,1,0,-1]
def move(r,c, d, s): 
    nr,nc = 0,0
    if d == "N": 
        nr = r + dr[0] * s 
        nc = c + dc[0] * s
    elif d == "E": 
        nr = r + dr[1] * s 
        nc = c + dc[1] * s
    elif d == "S":
        nr = r + dr[2] * s 
        nc = c + dc[2] * s 
    elif d == "W": 
        nr = r + dr[3] * s 
        nc = c + dc[3] * s 
    return nr,nc 
r,c = 0, 0
for _ in range(N): 
    d, s = input().split() 
    s = int(s) 
    nr, nc = move(r,c,d,s)
    r,c = nr,nc 
print(nc, nr)