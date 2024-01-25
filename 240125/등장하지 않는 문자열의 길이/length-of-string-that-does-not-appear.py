# 부분문자열들을 구해야겠다 우선은 
N = int(input()) 
s = input() 
ans = 1 
# 1씩 늘려가기 
for i in range(1,N): 
    # 모든 길이가 i인 부분 문자열에 대해 쌍을 짓고 같은지 확인 
    twice = False 
    for j in range(N-i+1): 
        for k in range(j+1, N-i+1): 
            # issame: 부분 문자열이 같은지 확인 
            issame = True 
            for l in range(i): 
                if s[j+l] != s[k+l]: 
                    issame = False 
            if issame: 
                twice = True 
    if twice: 
        ans = i + 1 
    else: 
        break 
print(ans)