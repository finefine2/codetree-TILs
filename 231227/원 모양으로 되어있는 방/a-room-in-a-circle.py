# my solution - using several functions for cal

# N = int(input())
# circles = []
# for _ in range(N): 
#     circles.append(int(input()))

# def repos(start,arr): 
#     new_circles = arr[start:] + arr[:start] 
#     return new_circles
# ans = 1e9 

# def cal_sum(arr): 
#     ans = 0
#     for i in range(1,len(arr)):
#         ans += arr[i] * abs(i)
#     return ans 
    
# for i in range(N): 
#     new_circles = repos(i,circles) 
#     sum_num = cal_sum(new_circles)
#     ans = min(sum_num,ans) 
# print(ans) 

# given solution 
# 각 방에서 시작할 때의 거리를 모두 계산
# 시작하는 방 번호 고르고, 각 방 까지의 거리 잰 뒤, 방에 할당된 인원수만큼 계산
min_dist = 1e9 
N = int(input()) 
arr = [int(input()) for _ in range(N)] 

# i 번째 방을 출발지로 고를 경우 
for i in range(N): 
    sum_dist = 0 
    for j in range(N): 
        # N보다 커질 경우를 대비해서 이처럼 진행한듯? 
        dist = (j+N-i) % N 
        sum_dist += dist * arr[i] 
    min_dist = min(min_dist,sum_dist)
print(min_dist)