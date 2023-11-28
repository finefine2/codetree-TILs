in_s = input() 
target = input() 
ans = -1
def check_s(): 
    global in_s, target, ans
    # 8, 2 
    # 0 1 2 3 4 5
    for i in range(len(in_s) - len(target)+1):
        if target == in_s[i:i+len(target)]: 
            ans = i 
            break 

    return False 
check_s()
print(ans)