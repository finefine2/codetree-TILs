# def modify(string): 
#     string += "apple" 
#     return string 

# _str = "banana" 
# _str = modify(_str)

# print(_str)
A = input()

def check_palin(s): 
    if s == s[::-1]: 
        print("Yes") 
    else: 
        print("No") 
check_palin(A)