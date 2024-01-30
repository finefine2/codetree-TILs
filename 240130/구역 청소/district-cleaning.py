a,b = map(int,input().split()) 
c,d = map(int,input().split()) 
sect = [0] * 101 

for i in range(101): 
    if a <= i <= b: 
        sect[i] += 1 
    if c <= i <= d: 
        sect[i] += 1 
cnt = 0 
for s in sect: 
    if s != 0: 
        cnt += 1 
print(cnt-1)