N = int(input())
A = input()
ans = 0 
for i in range(N): 
    for j in range(i+1,N): 
        for k in range(j+1,N): 
            if A[i] == "C" and A[j] == "O" and A[k] == "W": 
                ans += 1 
print(ans)