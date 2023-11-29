a,b,c = map(int,input().split()) 

def sum_num(n): 
    if n // 10 == 0:
        return n % 10 
    return n % 10 + sum_num(n//10) 
print(sum_num(a*b*c))