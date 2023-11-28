a,b = map(int,input().split()) 

def calc(n1,n2): 
    if n1 > n2: 
        n1 *= 2 
        n2 += 10 
    else: 
        n1 += 10
        n2 *= 2 
    return n1, n2 

a,b = calc(a,b) 
print(a, b)