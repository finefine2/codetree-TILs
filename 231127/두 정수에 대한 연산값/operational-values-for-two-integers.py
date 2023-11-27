a,b = map(int,input().split()) 

def big(num1,num2): 
    if num1 > num2: 
        num1 = num1 + 25 
        num2 = num2 * 2 
    else: 
        num2 = num2 + 25 
        num1 = num1 * 2
    
    return num1, num2 

a,b = big(a,b) 
print(a, b)