N = int(input()) 
nums = list(map(int,input().split())) 

def insert_sort(): 
    for i in range(1,N): 
        j, key = i-1, nums[i] 
        while j >= 0 and nums[j] > key: 
            nums[j+1] = nums[j] 
            j -= 1 
        nums[j+1] = key 
insert_sort()

for n in nums: 
    print(n, end = " ")