N = int(input()) 

# 검은색은 -1 
# 흰색은 1 
OFFSET = 10000

lines = [0] * 20001 
pos = [] 
start = OFFSET
for _ in range(N): 
    x, d = input().split() 
    x = int(x) 
    
    # left --> white. let it be 1
    if d == "L": 
        for i in range(start,start-x-1,-1): 
            lines[i] = 1
        start = start - x
    # right --> black. let it be -1 
    elif d == "R":
        for i in range(start,start+x+1): 
            lines[i] = -1
        start = start + x 
ans1, ans2 = 0,0
for l in lines:
    if l == 1: 
        ans1 += 1 
    elif l == -1: 
        ans2 += 1 
print(ans1-1, ans2)