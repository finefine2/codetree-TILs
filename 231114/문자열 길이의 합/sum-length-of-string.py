n = int(input()) 
chars = [] 
for _ in range(n): 
    chars.append(input()) 

cnt = 0
le = 0 
for c in chars: 
    le += len(c) 
    if c[0] == 'a': 
        cnt += 1 

print(le, cnt)