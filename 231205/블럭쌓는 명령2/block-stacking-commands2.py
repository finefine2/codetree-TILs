N,K = map(int,input().split()) 

nums = [0] *(1+N)

def sort_arr(start,end): 
    global nums 
    for i in range(start,end+1): 
        nums[i] += 1 

for _ in range(K): 
    A,B = map(int,input().split()) 
    sort_arr(A,B)
print(max(nums))