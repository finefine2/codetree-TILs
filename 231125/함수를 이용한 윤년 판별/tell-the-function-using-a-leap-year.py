def lunar_year(n): 
    if n % 4 == 0: 
        return True 
    if n % 4 == 0 and n % 100 == 0: 
        return False 
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0: 
        return True 
    return False 

    
n = int(input()) 

if lunar_year(n): 
    print("true") 
else: 
    print("false")