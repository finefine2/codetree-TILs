N = int(input()) 

nums = list(map(int,input().split())) 

unique_nums = list(set(list(nums))) 

if len(unique_nums) == 0: 
    print(-1) 
else:
    print(max(unique_nums))