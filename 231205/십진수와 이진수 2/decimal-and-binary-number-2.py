N = list(map(int,list(input()))) 
def convert_decimal(bnum): 
    ans = 0 
    for i in range(len(bnum)): 
        ans = ans * 2 + bnum[i] 
    return ans 
    

def convert_binary(num): 
    ans = []
    while True: 
        if num < 2: 
            ans.append(num) 
            break 
        ans.append(num % 2) 
        num //= 2 
        return ans[::-1] 

dnum = convert_decimal(N)
dnum *= 17 
ans = [] 
while True: 
    if dnum < 2: 
        ans.append(dnum)
        break 
    ans.append(dnum % 2) 
    dnum //= 2
for a in ans[::-1]: 
    print(a,end="")