def print_n(n): 
    if n == 0: 
        return 
    print(n,end=" ") 
    print_n(n-1) 
    print(n,end=" ") 

N = int(input()) 
print_n(N)