cnt = 0 
ans = [] 
while True: 
    s = input()
    if s == '0': 
        print(cnt) 
        break 
    cnt += 1 
    if cnt % 2 == 1: 
        ans.append(s)
for a in ans: 
    print(a)