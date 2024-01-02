# nums = list(map(int,input().split())) 

# def get_diff(i,j): 
#     sum1 = nums[i] + nums[j] 
#     sum2 = sum(nums) - sum1 
#     return abs(sum1-sum2)
# min_diff = 100 
# for i in range(len(nums)): 
#     for j in range(i+1,len(nums)): 
#         min_diff = min(min_diff, get_diff(i,j)) 
# print(min_diff)

# 6명을 3명으로 나누는데 
# 먼저 3명 조합이나 구해버리고 다른 팀은 전체 합에서 빼버리면 됨 

nums = list(map(int,input().split()))
total = sum(nums) 
team1,team2 = 0,0 
ans = 1e9 
for i in range(len(nums)): 
    for j in range(i+1, len(nums)): 
        for k in range(j+1, len(nums)): 
            team1 = nums[i] + nums[j] + nums[k] 
            team2 = total - team1 
            ans = min(ans,abs(team1-team2))
print(ans)