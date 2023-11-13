in_x = input() 
chrs = ["apple","banana","grape","blueberry","orange"] 

cnt = 0 
for c in chrs: 
    if in_x == c[3] or in_x == c[2]: 
        print(c)
        cnt += 1 

print(cnt)