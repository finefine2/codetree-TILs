# R,k = 10, 5 
# nums = list(map(int,input().split()))
# placed = [0] * (1+R)

# for elem in nums: 
#     placed[elem] = 1
# max_cnt = 0 
# for i in range(1,R-k+2): 
#     candy_num = 0 
#     for j in range(i,i+k): 
#         candy_num += placed[j] 
#     max_cnt = max(max_cnt, candy_num) 
# print(max_cnt) 

N, K = map(int,input().split()) 
nums = [0] * 10000

for _ in range(N): 
    n, s = input().split() 
    n = int(n)
    if s == 'G': 
        nums[n] = 1
    elif s == 'H': 
        nums[n] = 2
ans = 0
for i in range(len(nums)-K): 
    score = 0 
    for j in range(i,i+K+1): 
        score += nums[j] 
    ans = max(score, ans) 
print(ans)