N = int(input())

def get_seq(n): 
    if n == 1: 
        return 1 
    if n == 2: 
        return 2 

    return get_seq(n//3) + get_seq(n-1) 
print(get_seq(N))