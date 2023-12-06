lines = [0] * 10000
start = 5000
N = int(input()) 

for _ in range(N): 
    x,d = input().split()
    x = int(x) 
    if d == "R": 
        for i in range(start,start+x+1): 
            lines[i] += 1
        start = start + x
    elif d == "L": 
        for i in range(start,start-x-1,-1):
            lines[i] += 1
        start = start - x 
cnt = [] 
for i in range(len(lines)): 
    if lines[i] > 1: 
        cnt.append(i) 
ans = 0 

for i in range(len(cnt)-1): 
    if cnt[i+1] - cnt[i] == 1:
        ans += 1
print(ans)