nums = list(map(int,input().split())) 
total = sum(nums) 
s1, s2, s3 = 0, 0, 0
min_ans = 1e9 

for i in range(6):
    for j in range(1,6): 
        for k in range(2,6): 
            for l in range(3,6):
                s1 = nums[i] + nums[j] 
                s2 = nums[k] + nums[l] 
                s3 = total - s1 - s2 
                if s1 == s2 or s2 == s3 or s1 == s3: 
                    continue
                min_ans = min(min_ans,max(s1,s2,s3) - min(s1,s2,s3))
print(min_ans)