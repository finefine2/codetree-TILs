a,b = map(int,input().split()) 

def big(num1,num2): 
    ans1, ans2 = 0, 0
    ans1 = max(num1,num2) + 25 
    ans2 = min(num1,num2) * 2 

    return ans2, ans1

a,b = big(a,b) 
print(a, b)