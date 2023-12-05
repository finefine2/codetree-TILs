a,b = map(int,input().split()) 
n = list(map(int,list(input())))
# a 진수 -> 10진수 -> b진수 

def convert_decimal(num): 
    ans = 0 
    for i in range(len(num)): 
        ans = ans * a + num[i] 

    return ans 

def convert_b(dnum): 
    ans = []    
    while True: 
        if dnum < b: 
            ans.append(dnum)
            break 
        ans.append(dnum % b) 
        dnum //= b 
    return ans 

ans = convert_b(convert_decimal(n))
for a in ans[::-1]: 
    print(a,end="")