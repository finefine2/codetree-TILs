'''
def print_star(n): 
    if n == 0: 
        return 
    print_star(n-1) 
    print("*" * n) 
*
**
***
def print_star(n): 
    if n == 0: 
        return 
    print("*" * n) 
    print_star(n-1) 
***
**
*
def print_star(n): 
    if n == 0: 
        return 
    print("*" * n) 
    print_star(n-1) 
    print("*" * n) 
***
**
*
*
**
***
'''


N = int(input()) 

def print_num_first(n): 
    if n == 0: 
        return
    print_num_first(n-1)
    print(n,end=" ")
def print_num_sec(n): 
    if n == 0: 
        return
    print(n,end=" ")
    print_num_sec(n-1) 
print_num_first(N)
print()
print_num_sec(N)