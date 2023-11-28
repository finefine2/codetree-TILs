n,m = map(int,input().split()) 
nums = list(map(int,input().split())) 

def calc(n1,n2): 
    global nums 
    ans = 0 
    for i in range(a1-1,a2): 
        ans += nums[i] 
    return ans 

for _ in range(m): 
    a1,a2 = map(int,input().split()) 
    ans = calc(a1,a2) 
    print(ans)