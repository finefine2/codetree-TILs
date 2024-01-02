N, K = map(int,input().split()) 
placed = [0] * 100

for _ in range(N): 
    c, p = map(int,input().split()) 
    placed[p-1] = c 
ans = -5000
for i in range(K,len(placed)-K): 
    ans = max(ans,sum(placed[i-K:i+K+1]))
print(ans)