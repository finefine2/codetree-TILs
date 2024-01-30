N = int(input()) 

lines = [] 
for _ in range(N): 
    x1,x2 = map(int,input().split()) 
    lines.append([x1,x2]) 
flag = False 
def check(arr): 
    global N 
    check = [0] * 101 
    for a,b in arr: 
        for i in range(a,b+1): 
            check[i] += 1 
    for c in check: 
        if c == N-1: 
            return True 
for i in range(N): 
    tmp = []
    for j in range(N): 
        if i == j: 
            continue 
        tmp.append(lines[j]) 
    if check(tmp): 
        flag = True 
    
if flag: 
    print("Yes")
else: 
    print("No")