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

# N 이 1이 되면 끝나는 조건임 
# N 이 1이 아니면 나누고 카운트를 추가해야한다 
cnt = 0 
def calc(n): 
    global cnt 
    cnt += 1 
    if n == 1: 
        return cnt 
    
    if n % 2 == 0: 
        return calc(n//2) 
    else: 
        return calc(n//3) 
calc(N) 
print(cnt-1)