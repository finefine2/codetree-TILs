# N = int(input()) 
# ans = 0
# for i in range(1,N+1): 
#     ans += i 
# print(ans)

N = int(input()) 

def recur_sum(n): 
    if n == 0: 
        return 0 
    return recur_sum(n-1) + n 
print(recur_sum(N))