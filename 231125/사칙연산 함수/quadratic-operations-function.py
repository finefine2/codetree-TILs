num1, o, num2 = input().split() 

def calc(num1,num2,o): 
    ans = 0
    num1 = int(num1) 
    num2 = int(num2) 
    
    if o == "+": 
        return num1 + num2 
    elif o == "-": 
        return num1 - num2 
    elif o == "/": 
        return int(num1 / num2)
    elif o == "*": 
        return num1 * num2 
    else: return False 

ans = calc(num1,num2,o)
if ans: 
    print("{} {} {} = {}".format(num1,o,num2,ans))
else: 
    print("False")