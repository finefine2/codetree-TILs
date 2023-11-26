n1, n2 = map(int,input().split()) 
A = list(map(int,input().split())) 
B = list(map(int,input().split())) 

def check_seq(s1,s2): 
    for i in range(0,len(s1)-len(s2)): 
        if s1[i:i+len(s2)] == s2: 
            return True 
    return False 

def return_ans(A,B): 
    if check_seq(A,B): 
        print("Yes")
    else: 
        print("No") 

return_ans(A,B)