N = int(input()) 
nums = list(map(int,input().split())) 

def selection_sort(): 
    for i in range(N-1): 
        min_idx = i 
        for k in range(i+1,N): 
            if nums[min_idx] > nums[k]: 
                min_idx = k 
        nums[i], nums[min_idx] = nums[min_idx], nums[i] 
selection_sort() 

for n in nums: 
    print(n, end=" ")