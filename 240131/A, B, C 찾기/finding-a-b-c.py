nums = list(map(int,input().split()))

A = min(nums) 
X = max(nums) 
nums.pop(A) 
B = min(nums) 
C = X - A - B 

print(A, B, C)