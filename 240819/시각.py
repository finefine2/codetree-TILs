N = int(input()) 
# 매시간을 문자열로 바꾸고 3이 포함되었는지 확인해보기 

cnt = 0 
for i in range(N+1): 
    for j in range(60): 
        for k in range(60): 
            if '3' in str(i) + str(j) + str(k): 
                cnt += 1 
print(cnt)
