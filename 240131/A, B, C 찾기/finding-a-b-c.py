nums = list(map(int,input().split()))
nums.sort() 
A = min(nums) 
X = max(nums) 
# print(nums) 
nums.pop(0) 
# print(nums) 
B = min(nums) 
C = X - A - B 

print(A, B, C)