n,m = map(int,input().split()) 
arr = [0] + list(map(int,input().split())) 

def calc(): 
    global m 
    ans = 0 
    while m: 
        ans += arr[m] 
        if m % 2 == 0: 
            m //= 2 
        else: 
            m -= 1
    return ans 
print(calc())