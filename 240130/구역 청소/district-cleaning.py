a,b = map(int,input().split()) 
c,d = map(int,input().split()) 
sect = [0] * 101 

for i in range(a,b): 
    sect[i] += 1 
for i in range(c,d): 
    sect[i] += 1 

cnt = 0 
for s in sect: 
    if s != 0: 
        cnt += 1 
print(cnt)