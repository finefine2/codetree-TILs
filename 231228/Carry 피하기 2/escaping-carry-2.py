# my solution 
# N = int(input()) 
# nums = [int(input()) for _ in range(N)] 
# def carry(a,b,c): 
#     max_len = max(len(str(a)), len(str(b)), len(str(c)))
#     cnt = 0 
#     while a > 0 or b > 0 or c > 0: 
#         if (a % 10 + b % 10 + c % 10) >= 10: 
#             break 
#         elif (a % 10 + b % 10 + c % 10) < 10: 
#             a //= 10 
#             b //= 10 
#             c //= 10
#             cnt += 1
#     if cnt == max_len: 
#         return True 
#     else: 
#         return False

# ans = -1
# # 완탐 돌리기 
# for i in range(N): 
#     for j in range(i+1,N):
#         for k in range(j+1,N): 
#             if carry(nums[i],nums[j],nums[k]): 
#                 ans = max(ans, nums[i] + nums[j] + nums[k])
# print(ans) 

# given solution 
# 일의 자리, 십의 자리, 백의 자리, 천의 자리를 각각 더 해보기 
# 왜냐면 input 조건이 10000 미만이기떄문
N = int(input())
nums = [int(input()) for _ in range(N)] 

ans = -1 
for i in range(N): 
    for j in range(i+1,N): 
        for k in range(j+1,N):
            carry = False 
            a,b,c = nums[i],nums[j],nums[k]
            # 일의 자리 check
            if a % 10 + b % 10 + c % 10 >= 10: 
                carry = True             
            # 십의 자리 check
            if a % 100 // 10 + b % 100 // 10 + c % 100 // 10 >= 10: 
                carry = True 
            # 백의 자리 check 
            if a % 1000 // 10 + b % 1000 // 10 + c % 1000 // 10 >= 10: 
                carry = True
            # 천의 자리 check
            if a % 10000 // 10 + b % 10000 // 10 + c % 10000 // 10 >= 10: 
                carry = True
            if carry == False: 
                ans = max(ans, a+b+c)
print(ans)