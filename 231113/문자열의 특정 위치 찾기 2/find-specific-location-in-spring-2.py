in_x = input() 
chrs = ["apple","banana","grape","blueberry","orange"] 
ans = [] 
cnt = 0 
for c in chrs: 
    if in_x == c[3] or in_x == c[2]: 
        ans.append(c)
        cnt += 1 
    
if len(ans) == 0: 
    print(0) 
else: 
    for a in ans: 
        print(a)
    print(cnt)