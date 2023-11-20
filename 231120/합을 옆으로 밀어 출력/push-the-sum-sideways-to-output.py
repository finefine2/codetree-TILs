n = int(input()) 

nums = [] 
for _ in range(n): 
    nums.append(int(input()))

ans_n = sum(nums) 
ans_s = str(ans_n)

ans = ans_s[1:] +ans_s[0] 

print(ans)