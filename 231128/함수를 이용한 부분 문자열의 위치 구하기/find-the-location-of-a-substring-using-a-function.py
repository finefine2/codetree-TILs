in_s = input() 
target = input() 

def check_s(): 
    global in_s, target
    # 8, 2 
    # 0 1 2 3 4 5

    for i in range(len(in_s) - len(target)+1):
        if target == in_s[i:i+len(target)]: 
            return i 

    return False 

if not check_s(): 
    print(-1) 
else: 
    print(check_s())