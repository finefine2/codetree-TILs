# my solution 
# N = int(input()) 
# cnt = 0 
# def get_count(n): 
#     global cnt 
#     if n == 1: 
#         return cnt + 1
#     if n % 2 != 0: 
#         cnt += 1
#         return get_count(n * 3 + 1)
#     else: 
#         cnt += 1
#         return get_count(n // 2) 
    
# print(get_count(N) -1 )

# given solution 

'''
f(1) = 0. 1에서 시작하면 바로 끝나기 때문에 앞으로 필요한 횟수는 0 
n이 짝수면 f(n) = f(n/2) + 1 
n이 홀수면 f(n) = f(3*n+1) + 1 
'''
N = int(input()) 

def get_count(n): 
    if n == 1: 
        return 0 
    if n % 2 == 0:
        return get_count(n // 2) + 1 
    else: 
        return get_count(3 * n + 1) + 1 
print(get_count(N))