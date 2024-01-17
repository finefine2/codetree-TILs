# 일단 전부 골라보자 
# n-3 개 선분들을 전부 고른다
# 그리고 겹치는지 안 겹치는지 체크한다 
N = int(input()) 
lines = [tuple(map(int,input().split())) for _ in range(N)] 

def check_overlap(a,b,c): 
    count = [0] * 101
    ans = True
    for i in range(N): 
        if i in [a,b,c]: 
            continue
        x1, x2 = lines[i] 
        # print(i)
        # print(x1,x2) 
        for j in range(x1,x2+1): 
            count[j] += 1
        # print(count) 
        if 2 not in count: 
            ans = True 
        else: 
            ans = False 
            break 
              
    return ans 

ans = 0
for i in range(N): 
    for j in range(i+1,N): 
        for k in range(j+1,N): 
            if check_overlap(i,j,k): 
                ans += 1 
print(ans)