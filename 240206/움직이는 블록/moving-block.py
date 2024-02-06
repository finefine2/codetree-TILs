N = int(input()) 

blocks = [int(input()) for _ in range(N)] 

sum_block = sum(blocks) 
avg = sum_block // N 
ans = 0 

for b in blocks: 
    if b > avg: 
        ans += (b - avg) 
print(ans)