N = int(input()) 

points = [] 
for _ in range(N): 
    r,c = map(int,input().split()) 
    points.append([r,c]) 

def count_point(a,b,points): 
    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0
    for r,c in points: 
        if r < a and c < b: 
            cnt1 += 1 
        elif r < a and c > b: 
            cnt2 += 1 
        elif r > a and c < b: 
            cnt3 += 1 
        elif r > a and c > b: 
            cnt4 += 1 
    return cnt1, cnt2, cnt3, cnt4 

ans = 1e9 
for i in range(2,101,2): 
    for j in range(2,101,2): 
        line_r, line_c = i, j
        cnt1,cnt2,cnt3,cnt4 = count_point(i,j,points) 
        cnt = max(cnt1,cnt2,cnt3,cnt4) 
        ans = min(cnt,ans) 
print(ans)