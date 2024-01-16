K, N = map(int,input().split())
results = [list(map(int,input().split())) for _ in range(K)]
people = [int(i) for i in range(1,N+1)] 

cnt = 0 

# 먼저 NC2 조합을 구해보고 조건에 만족을 하는 지 체크를 해보자 

pos = [] 
for i in range(N): 
    for j in range(N):
        if j == i: 
            continue 
        pos.append([people[i],people[j]]) 

cnt = 0 
for p in pos: 
    flag = True 
    for r in results: 
        num1, num2 = p[0], p[1] 
        tmp1, tmp2 = 0, 0
        for i in range(N): 
            if num1 == r[i]: 
                tmp1 = i 
            elif num2 == r[i]: 
                tmp2 = i 
        # print(num1,num2)
        # print(tmp1,tmp2)
        # print("##########")
        if tmp1 > tmp2: 
            flag = False 
            break 
    if flag: 
        cnt += 1
print(cnt)