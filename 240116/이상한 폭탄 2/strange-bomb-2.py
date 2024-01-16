'''
my solution 
'''
# N, K = map(int,input().split()) 
# bombs = [int(input()) for _ in range(N)] 
# ans = [] 
# for i in range(N): 
#     for j in range(N): 
#         if j == i: 
#             continue 
#         if abs(j-i) <= K and bombs[i] == bombs[j]: 
#             ans.append(bombs[i]) 
# if len(ans) == 0: 
#     print(-1) 
# else: 
#     print(max(ans))

'''
모든 폭탄에 대해, 나머지 폭탄 중 번호가 같고 거리가 k 이내인 폭탄이 있는지 찾아보고, 최댓값을 갱신하자 
how to solve? 
각 폭탄마다 폭발하는 경우를 찾고, 폭발한다면 최댓값을 갱신 
'''
N,K = map(int,input().split())
bombs = [list(map(int,input().split())) for _ in range(N)] 

ans = -1 
# 모든 쌍에 대해 터질 수 있는 폭탄을 찾고 그 중 최댓값을 리턴 
for i in range(N): 
    for j in range(i+1,N): 
        if j - i > K: 
            break 
        # if number of bombs differs, doesn't explode 
        if bombs[i] != bombs[j]: 
            continue
        ans = max(ans,bombs[i]) 
print(ans)