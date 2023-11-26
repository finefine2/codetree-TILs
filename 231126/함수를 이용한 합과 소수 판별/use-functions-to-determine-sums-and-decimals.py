def is_prime(n): 
    if n == 1: 
        return False 
    for i in range(2,n): 
        if n % i == 0: 
            return False 
    return True 

def is_even(n): 
    ans = 0
    n_str = str(n)
    for s in n_str: 
        ans += int(s) 
    if ans % 2 == 0: 
        return True 
    return False

a,b = map(int,input().split()) 
cnt = 0  
for i in range(a,b+1): 
    if is_prime(i) and is_even(i):  
        cnt += 1 
print(cnt)