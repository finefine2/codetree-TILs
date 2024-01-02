# my sol
# N,H,T = map(int,input().split())
# nums = list(map(int,input().split())) 
# # N 6 
# # 길이 3 
# # 부분집합 길이 3 
# ans = 1e9 

# def convert(arr): 
#     global H
#     cnt = 0  
#     for a in arr: 
#         if a != H: 
#             cnt += abs(a-H) 
#         elif a == H:
#             continue 
#     return cnt 
# for i in range(len(nums)-T+1): 
#     # 부분집합을 만든다 
#     pos = nums[i:i+T]
#     cnt = convert(pos)
#     ans = min(cnt,ans) 
# print(ans) 

# given solution 
N,H,T = map(int,input().split()) 
arr = list(map(int,input().split())) 

min_cost = 1e9 
# 모든 구간을 다 잡아본다 
# 전부 H가 되기 위한 길이 T구간을 잡아본다 
for i in range(N- T + 1): 
    cost = 0 
    for j in range(i,i+T): 
        cost += abs(arr[j] - H) 
    min_cost = min(min_cost,cost) 
print(min_cost)