# mine
# N,M = map(int,input().split()) 
# nums_A = list(map(int,input().split())) 
# nums_B = list(map(int,input().split())) 

# def compare_list(A,B): 
#     A.sort() 
#     B.sort() 
    
#     if A == B: 
#         return True 
#     else: 
#         return False 
# ans = 0
# for i in range(N-M+1): 
#     pos = nums_A[i:i+M] 
#     # 두 리스트가 같은지 판단하는 함수 
#     if compare_list(pos,nums_B): 
#         ans += 1 
# print(ans) 

# given solution 
N,M = map(int,input().split()) 
nums_A = list(map(int,input().split())) 
nums_B = list(map(int,input().split()))
# 모든 구간 시작점 카운트 
cnt = 0 
for i in range(N-M+1): 
    if sorted(nums_A[i:i+M]) == sorted(nums_B): 
        cnt += 1 
print(cnt)