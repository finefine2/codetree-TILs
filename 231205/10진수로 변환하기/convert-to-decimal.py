'''
from binary number to decimal  
'''

# 가장 왼쪽에서 시작하여 오른쪽 방향으로 한 칸씩 움직이며 구할 수 있음 
# num을 0번 idx부터 i번 idx 까지 10진법으로 변환한 값이라 생각. 
# num = prev_num * 2 + binary[i] 

# binary = [1,1,1,0,1]
# num = 0 

# for i in range(5): 
#     num = num * 2 + binary[i] 
# print(num)

# my solution 
# n = int(input()) 

# n_str = str(n) 
# nums = []

# for i in range(len(n_str)): 
#     nums.append(int(n_str[i]))

# ans = 0 

# for i in range(len(nums)): 
#     ans = ans * 2 + nums[i] 
# print(ans) 

# given sol 
binary = list(map(int,list(input())))
ans = 0 
for i in range(len(binary)): 
    ans = ans * 2 + binary[i] 
print(ans)