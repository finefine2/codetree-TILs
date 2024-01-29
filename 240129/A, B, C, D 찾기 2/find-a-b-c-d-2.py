nums = list(map(int,input().split())) 

A = min(nums) 
def check(a,b,c,d): 
    global nums 
    tmp = [a,b,c,d,a+b,a+c,a+d,b+c,b+d,c+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d] 
    tmp.sort() 
    nums.sort() 
    if tmp == nums: 
        return True 
    else: 
        return False    

for i in range(A,41): 
    for j in range(i,41): 
        for k in range(j,41): 
            if check(A,i,j,k): 
                print(A,i,j,k)