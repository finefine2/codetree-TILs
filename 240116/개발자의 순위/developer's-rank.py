'''
# 먼저 NC2 조합을 구해보고 조건에 만족을 하는 지 체크를 해보자 
'''
# K, N = map(int,input().split())
# results = [list(map(int,input().split())) for _ in range(K)]
# people = [int(i) for i in range(1,N+1)] 

# cnt = 0 

# pos = [] 
# for i in range(N): 
#     for j in range(N):
#         if j == i: 
#             continue 
#         pos.append([people[i],people[j]]) 

# cnt = 0 
# for p in pos: 
#     flag = True 
#     for r in results: 
#         num1, num2 = p[0], p[1] 
#         tmp1, tmp2 = 0, 0
#         for i in range(N): 
#             if num1 == r[i]: 
#                 tmp1 = i 
#             elif num2 == r[i]: 
#                 tmp2 = i 
#         # print(num1,num2)
#         # print(tmp1,tmp2)
#         # print("##########")
#         if tmp1 > tmp2: 
#             flag = False 
#             break 
#     if flag: 
#         cnt += 1
# print(cnt) 


'''
given solution
'''
K,N = map(int,input().split()) 
arr = [list(map(int,input().split())) for _ in range(K)] 

ans = 0 
# 모든 쌍에 대해 불변 순위인 쌍을 찾자 
for i in range(1,N+1): 
    for j in range(1,N+1): 
        # i번 개발자가 j번보다 항상 높은 순위인지 체크 
        # i j 가 같으면 넘어감 
        if i == j: 
            continue
        # i번 개발자가 j보다 항상 높은 순위면 맞음 
        flag = True 
        # 모든 경기에 대해 두 개발자의 위치를 찾고, 하나라도 i번이 뒤에 있으면 false 로 바꿈 
        for ar in arr: 
            idx_i = ar.index(i) 
            idx_j = ar.index(j) 
            # list.index 기법을 까먹지 말 것 
            if idx_i > idx_j: 
                flag = False 
        if flag: 
            ans += 1 
print(ans)