def gcd(num1,num2): 
    ans = 0 
    small_num = min(num1,num2)
    for i in range(1,small_num+1): 
        if num1 % i == 0 and num2 % i == 0: 
            ans = i 
    return ans 


def lcm(num1,num2): 
    gc = gcd(num1,num2)
    ans = 0
    for i in range(1,100): 
        ans = gc * i 
        if ans % num1 == 0 and ans % num2 == 0: 
            print(ans) 
            break 


n,m = map(int,input().split()) 
lcm(n,m)