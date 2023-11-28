# 각 자리 숫자 합 
# 문자열로 접근 말고 10으로 나눈 나머지 구하기 
# def f(n): 
#     if n < 10: 
#         return n 
#     return f(n//10) + (n % 10) 

N = int(input()) 

def recur_power(n): 
    if n < 10: 
        return n * n 
    return recur_power(n//10) + (n % 10) ** 2 
print(recur_power(N))