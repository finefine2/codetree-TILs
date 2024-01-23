X, Y = map(int,input().split()) 
def check(num): 
    s = str(num) 
    if s == s[::-1]: 
        return True 
    else: 
        return False 
ans =  0 
for i in range(X,Y+1): 
    if check(i): 
        ans += 1 
print(ans)