'''
너무 어렵게 생각하고 있는 건 아닌가?
'''

# N = int(input()) 
# nums = []
# for _ in range(N): 
#     num, c1, c2 = map(int,input().split()) 
#     num = list(map(int,str(num))) 
#     nums.append([num[0],num[1],num[2],c1,c2])

# cnt = 0 
# for i in range(1,10): 
#     for j in range(1,10): 
#         for k in range(1,10): 
#             if i == j or j == k or i == k: 
#                 continue 
#             flag = True 
#             for num in nums: 
#                 cnt1, cnt2 = 0,0 
#                 tmp = [i,j,k] 
#                 for l in range(3): 
#                     for q in range(3): 
#                         if num[l] == tmp[q]: 
#                             if l == q: 
#                                 cnt1 += 1 
#                             else: 
#                                 cnt2 += 1
#                 if cnt1 != num[3] or cnt2 != num[4]: 
#                     flag = False 
#             if flag: 
#                 cnt += 1 
# print(cnt) 

# B가 물어본 숫자와 특정 숫자를 백, 십, 일의 자리별로 비교하며 1번 카운트와 2번 카운트 값을 정함 
# B가 물어본 수는 각 자리 수가 서로 다르므로, 각 자리수 중 같은 수가 있다면 제외 
# 자리와 값이 같아야 1번 카운트가 증가, 값이 같지만 자리가 다르면 2번 카운트가 증가, 직접 증가시킨 1번 카운트와 2번 카운트가 
# 문제에서 주어진 값과 같아야 함 

N = int(input()) 
nums = [tuple(map(int,input().split())) for _ in range(N)] 

# 모든 숫자를 생성해보기 
ans = 0 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            if i == j or j == k or k == i: 
                continue
            flag = True 
            for num, cnt1, cnt2 in nums: 
                x = num // 100 
                y = num //10 % 10 
                z = num % 10 
                c1, c2 = 0,0 
                if x == i: 
                    c1 += 1 
                if y == j: 
                    c1 += 1 
                if z == k: 
                    c1 += 1 
                if x == j or x == k: 
                    c2 += 1
                if y == i or y == k: 
                    c2 += 1 
                if z == i or z == j: 
                    c2 += 1
                if cnt1 != c1 or cnt2 != c2: 
                    flag = False 
                    break 
            if flag: 
                ans += 1 
print(ans)