N = int(input()) 

# def sum_num(n): 
#     if n % 2 == 0:
#         if n == 2: 
#             return 2 
#         return n + sum_num(n//2) 
#     else: 
#         if n == 1: 
#             return 1 
#         return n + sum_num(n//2)
# print(sum_num(N))
ans = 0
if N % 2 == 0:  
    for i in range(2, N+1, 2): 
        ans += i 
    print(ans) 
else: 
    for i in range(1,N+1,2): 
        ans += i 
    print(ans)