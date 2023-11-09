''' itertools 사용한 풀이 
from itertools import combinations 

N = int(input()) 
nums = list(map(int,input().split()))
numbers = combinations(nums,2) 

min_val = 1000

for n1,n2 in numbers: 
    if min_val > abs(n1-n2): 
        min_val = abs(n1-n2) 
print(min_val)
'''

N = int(input()) 
nums = list(map(int,input().split())) 

# 숫자들이 오름차순으로 주어짐 
# 두 숫자 최솟값은 반드시 인접한 두 숫자의 차이 중에 있음 
# 초기값 적고, 비교 

min_val = nums[1] - nums[0] 
for i in range(2,N): 
    if min_val > nums[i] - nums[i-1]: # 지금까지 나온 값들보다 더 작으면 
        min_val = nums[i] - nums[i-1] #  갱신
print(min_val)