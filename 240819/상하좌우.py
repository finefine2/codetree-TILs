# 아주 오랜만에 쑥쑥 풀어버림
N = int(input()) 
movements = input().split()

drs,dcs = [0,0,-1,1],[-1,1,0,0]

def in_range(r,c): 
  return 0 <= r < N and 0 <= c <N 
start_r, start_c = 0,0 

def move(r,c,d):
    nr, nc = 0,0
    if d == "L":
        nr, nc = r + drs[0], c + dcs[0]
    elif d == "R":
        nr, nc = r + drs[1], c + dcs[1]
    elif d == "U":
        nr, nc = r + drs[2], c + dcs[2]
    elif d == "D":
        nr, nc = r + drs[3], c + dcs[3]
    return nr, nc

for m in movements: 
  nr, nc = move(start_r,start_c,m)
  if not in_range(nr,nc): 
    continue 
  else: 
    start_r, start_c = nr, nc 
print(start_r+1,start_c+1) 
