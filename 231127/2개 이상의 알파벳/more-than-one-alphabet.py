A = input() 
def count(s): 
    cnt = 0 
    for i in range(len(s)-1): 
        if s[i] != s[i-1]: 
            cnt += 1
    if cnt >= 2: 
        return True 
    return False 

if count(A): 
    print("Yes") 
else: 
    print("No")