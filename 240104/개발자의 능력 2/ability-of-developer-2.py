nums = list(map(int,input().split())) 
total = sum(nums)

sum1,sum2,sum3 = 0,0,0 
min_ans = 1e9 
def get_diff(i,j,k,l): 
    sum1 = nums[i] + nums[j] 
    sum2 = nums[k] + nums[l] 
    sum3 = sum(nums) - sum1 - sum2 
    max_sum = max(sum1,sum2,sum3) 
    min_sum = min(sum1,sum2,sum3) 
    return max_sum - min_sum

for i in range(6): 
    for j in range(i+1,6): 
        for k in range(j+1,6): 
            for l in range(k+1,6): 
                
                min_ans = min(min_ans,get_diff(i,j,k,l))
print(min_ans-1)