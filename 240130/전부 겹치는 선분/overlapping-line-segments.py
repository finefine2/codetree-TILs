N = int(input()) 
lines = [] 
for _ in range(N): 
    x1,x2 = map(int,input().split()) 
    lines.append([x1,x2]) 

check = [0] * 101 
for x1,x2 in lines: 
    for i in range(x1,x2): 
        check[i] += 1 
import sys 

for c in check: 
    if c == N: 
        print("Yes") 
        sys.exit()
    else: 
        print("No")
        sys.exit()