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

# my solution 
# N = int(input()) 

# # N 이 1이 되면 끝나는 조건임 
# # N 이 1이 아니면 나누고 카운트를 추가해야한다 
# cnt = 0 
# def calc(n): 
#     global cnt 
#     cnt += 1 
#     if n == 1: 
#         return cnt 
    
#     if n % 2 == 0: 
#         return calc(n//2) 
#     else: 
#         return calc(n//3) 
# calc(N) 
# print(cnt-1) 

# given solution 
N = int(input())
# n 에서 시작하여 1이 되기 위해 필요한 횟수를 카운팅 
def get_num(n): 
    # 1이면 끝나므로 0회가 더 필요함 
    if n == 1: 
        return 0 
    # 짝수라면 2로 나눴을 때의 횟수 + 1번이 소요됨 
    if n % 2 == 0: 
        return get_num(n//2) + 1 
    # 홀수라면 3으로 나눈 몫으로 진행한 횟수 + 1번 
    else: 
        return get_num(n//3) + 1 
print(get_num(N))