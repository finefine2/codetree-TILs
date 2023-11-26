# my solution 
# def is_prime(n): 
#     if n == 1: 
#         return False 
#     for i in range(2,n): 
#         if n % i == 0: 
#             return False 
#     return True 

# def is_even(n): 
#     ans = 0
#     n_str = str(n)
#     for s in n_str: 
#         ans += int(s) 
#     if ans % 2 == 0: 
#         return True 
#     return False

# a,b = map(int,input().split()) 
# cnt = 0  
# for i in range(a,b+1): 
#     if is_prime(i) and is_even(i):  
#         cnt += 1 
# print(cnt) 

# given solution 
a,b = map(int,input().split()) 

def is_prime(n): 
    if n == 1: 
        return False 
    for i in range(2,n): 
        if n % i == 0: 
            return False
    return True 

def is_even(n): 
    digit_sum = (n//100) + ((n//10) % 10) + (n % 10) 
    if digit_sum % 2 == 0: 
        return True 
    return False 

cnt = 0 

def check_num(n): 
    if is_prime(n) and is_even(n): 
        return True 
    return False 

for i in range(a,b+1): 
    if check_num(i): 
        cnt += 1
print(cnt)