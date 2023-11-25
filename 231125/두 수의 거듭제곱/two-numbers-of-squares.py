def power(num1,num2): 
    ans = num1 
    for i in range(num2): 
        ans *= num1 
    return ans 
a,b = map(int,input().split())
print(power(a,b))