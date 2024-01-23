# # 잘 모르는 상황에 대해서는 일일이 값을 가정해보고 진행한다 

# max_cnt = 0 
# for i in range(1,10): 
#     num, cnt = i, 0 
#     while num != 1: 
#         if num % 2 == 0: 
#             num //= 2 
#         else: 
#             num = num * 3 + 1 
#         cnt += 1 
#     max_cnt = max(max_cnt,cnt) 
# print(max_cnt)

N = int(input()) 
stones = [] 
for _ in range(N): 
    a,b,c = map(int,input().split()) 
    stones.append([a-1,b-1,c-1])
# 조약돌을 1,2,3 위치 넣어보기 
ans = 0 
for i in range(3): 
    lines = [0] * 3
    lines[i] = 1 
    cnt = 0    
    for a,b,c in stones: 
        lines[a] ,lines[b] = lines[b], lines[a] 
        if lines[c] == 1: 
            cnt += 1
    ans = max(cnt,ans) 
print(ans)