n = int(input()) 

def decide(num): 
    n_str = str(num)
    cnt = 0 
    ans = ""
    for n in n_str: 
        cnt += int(n) 
    if num%2 == 0 and cnt%5 == 0: 
        ans = "Yes"
    else: 
        ans = "No"
    return ans 

print(decide(n))