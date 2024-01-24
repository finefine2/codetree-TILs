'''
my solution 
'''
# A,B,C = map(int,input().split()) 
# ans = 0 
# for i in range(1000):
#     for j in range(1000):
#         tmp = A * i + B * j 

#         if tmp <= C: 
#             ans = max(ans,tmp)
# print(ans) 

'''
given solution - A의 사용 횟수를 먼저 정하고, 그에 따라 가능한 B의 최대 횟수를 구해 C보다 작은 합 중 회대를 구한다 
'''
A,B,C = map(int,input().split())
ans = 0 
# A를 몇 회 사용할지 전부 시도 
# 모든 경우의 수에 대해 최대가 되도록 
for i in range(C // A + 1): 
    cnt = A * i 
    num_B = (C-cnt) // B 
    cnt += num_B * B 
    ans = max(ans,cnt) 
print(ans)