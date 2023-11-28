# f(n) = f(n을 10으로 나눈 몫) + (n을 10으로 나눈 나머지) 
# f(123) = f(12) + 7 

# def f(n): 
#     if n < 10: 
#         if n % 2 == 0: 
#             return 0 
#         else: 
#             return n 

#     remainder = n % 10 
#     if remainder % 2 == 0: 
#         return f(n // 10) 
#     else: 
#         return f(n // 10)  + remainder

N = int(input()) 

def count(n): 
    cnt = 0 
    new_n = 0 
    if n == 1: 
        return cnt + 1

    if n % 2 == 0: 
        new_n = int(n / 2)
        cnt += 1
        return count(new_n)  
    else: 
        new_n = n // 3 
        cnt += 1
        return count(new_n) 

print(count(N))