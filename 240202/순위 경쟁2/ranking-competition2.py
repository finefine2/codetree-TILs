N = int(input()) 
score = [] 
for _ in range(N): 
    c,s = input().split() 
    score.append((c,int(s))) 
cnt_a, cnt_b = 0,0 

def status(cnt_a,cnt_b): 
    if cnt_a > cnt_b: 
        return 1 
    elif cnt_b > cnt_a: 
        return 2 
    else: 
        return 3 

ans = 0 
for c,s in score: 
    if c == 'A': 
        if status(cnt_a,cnt_b) != status(cnt_a + s, cnt_b): 
            ans += 1 
        cnt_a += s 
    else: 
        if status(cnt_a,cnt_b) != status(cnt_a, cnt_b + s): 
            ans += 1 
        cnt_b += s 
print(ans)