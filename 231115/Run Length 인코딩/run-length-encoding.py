A = input() 
cnt = 0 
ans = [] 

for i in range(len(A)): 
    
    if i == 0: 
        ans.append(A[i]) 
        cnt = 1 
        ans.append(cnt) 
        continue 
    
    prev = ans[-2] 

    if prev == A[i]: 
        cnt += 1 
        ans[-1] = cnt 
    
    else: 
        ans.append(A[i]) 
        cnt = 1 
        ans.append(cnt) 
ans = [str(i) for i in ans] 
ans1 = 0 

for a in ans: 
    ans1 += len(a) 

print(ans1)
print("".join(ans))