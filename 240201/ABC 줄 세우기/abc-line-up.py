N = int(input())
people = [0] + list(input().split()) 
ans = 0 

for i in range(1,N+1): 
    x = chr(ord("A") + i - 1) 
    idx = 0 
    for j in range(1,N+1): 
        if people[j] == x: 
            idx = j 
    for j in range(idx-1,i-1,-1): 
        people[j], people[j+1] = people[j+1],people[j] 
        ans += 1 
print(ans)