N = int(input()) 
nums = []
for _ in range(N): 
    num, c1, c2 = map(int,input().split()) 
    num = list(map(int,str(num))) 
    nums.append([num[0],num[1],num[2],c1,c2])

cnt = 0 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            if i == j or j == k or i == k: 
                continue 
            flag = True 
            for num in nums: 
                cnt1, cnt2 = 0,0 
                tmp = [i,j,k] 
                for l in range(3): 
                    for q in range(3): 
                        if num[l] == tmp[q]: 
                            if l == q: 
                                cnt1 += 1 
                            else: 
                                cnt2 += 1
                if cnt1 != num[3] or cnt2 != num[4]: 
                    flag = False 
            if flag: 
                cnt += 1 
print(cnt)