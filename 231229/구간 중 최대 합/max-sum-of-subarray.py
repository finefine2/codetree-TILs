N,K = map(int,input().split()) 
nums = list(map(int,input().split())) 

max_val = 0 

for i in range(N-K):
    max_val = max(max_val,sum(nums[i:i+K])) 
print(max_val)