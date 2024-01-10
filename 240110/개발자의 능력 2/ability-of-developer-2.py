nums = list(map(int,input().split())) 
total = sum(nums) 
min_ans = 1e9 
nums.sort() 

for i in range(6):
    for j in range(i+1,6): 
        for k in range(6): 
            if k == i or k == j: 
                continue
            for l in range(k+1,6):
                if l == i or l == j:
                    continue
                s1 = nums[i] + nums[j] 
                s2 = nums[k] + nums[l] 
                s3 = total - s1 - s2 
                min_ans = min(min_ans,max(s1,s2,s3) - min(s1,s2,s3))

print(min_ans)