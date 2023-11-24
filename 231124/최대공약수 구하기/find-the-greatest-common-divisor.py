def gcd(num1,num2): 
    ans = 1 
    small_num = min(num1,num2) 
    for i in range(1,small_num+1): 
        if num1 % i == 0 and num2 % i == 0: 
            ans = i 
    
    print(ans)

n,m = map(int,input().split()) 
gcd(n,m)