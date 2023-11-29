N = int(input()) 

def sum_num(n): 
    if n == 1: 
        return 1 
    if n == 2: 
        return 2 
    return sum_num(n) + n 
print(sum_num(N))