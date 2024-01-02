N = int(input()) 
MAX_NUM = 100 
placed = [0] *(1+MAX_NUM) 

for _ in range(N): 
    p,a = input().split() 
    placed[int(p)] = a 
ans = 0 

for i in range(len(placed)): 
    for j in range(i+1,len(placed)):
        if placed[i] == 0 or placed[j] == 0: 
            continue
        cnt_G, cnt_H = 0,0

        for k in range(i,j+1): 
            if placed[k] == "G": 
                cnt_G += 1
            if placed[k] == "H": 
                cnt_H += 1
        if cnt_G == cnt_H or cnt_H == 0 or cnt_G == 0: 
            leng = abs(i-j) 
            ans = max(ans,leng) 
print(ans) 

# N = int(input()) 
# MAX_NUM = 100 
# placed = [0] * (1+MAX_NUM)

# for _ in range(N): 
#     p, a = input().split()
#     placed[int(p)] = 1 if a == "G" else 2 

# ans = 0 

# # 구간을 무작정 잡아보고 
# # G H 로만 구성되어있는지
# # 혹은 하나씩으로만 되어있는지 체크 

# for i in range(MAX_NUM+1): 
#     for j in range(i+1, MAX_NUM+1): 
#         # 사람있는지 확인
#         if placed[i] == 0 or placed[j] == 0: 
#             continue
#         cnt_G,cnt_H = 0,0
#         for k in range(i,j+1): 
#             if placed[k] == 1: 
#                 cnt_G += 1 
#             elif placed[k] == 2: 
#                 cnt_H += 1 
#         # 조건을 만족할 때 구간의 길이를 구해 최댓값과 비교 
#         if cnt_G == 0 or cnt_H == 0 or cnt_G == cnt_H: 
#             leng = j-i 
#             ans = max(leng,ans) 
# print(ans)