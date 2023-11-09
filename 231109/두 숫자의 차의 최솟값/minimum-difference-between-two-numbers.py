from itertools import combinations 

N = int(input()) 
nums = list(map(int,input().split()))
numbers = combinations(nums,2) 

min_val = 1000

for n1,n2 in numbers: 
    if min_val > abs(n1-n2): 
        min_val = abs(n1-n2) 
print(min_val)