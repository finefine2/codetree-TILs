N = int(input()) 
nums = list(map(int,input().split())) 

def gcd(n1,n2): 
    if n2 == 0: 
        return n1 
    return gcd(n2, n1 % n2)

def lcm(n1,n2): 
    return (n1 * n2) // gcd(n1,n2) 

ans = lcm(nums[0],nums[1]) 
for i in range(1,len(nums)-1): 
    ans = lcm(ans,nums[i+1])
print(ans)