# def recur_sum(n): 
#     ans = 0 
#     if n == 1: 
#         ans += 1 
#         print(ans)
#         return 
#     ans += n 
#     recur_sum(n-1) 

N = int(input()) 
ans = 0
for i in range(1,N+1): 
    ans += i 
print(ans)