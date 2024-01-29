N = int(input()) 

seats = list(input()) 
ans = 0 
def count(arr): 
    min_dist = 100
    for i in range(len(arr)): 
        for j in range(i+1,len(arr)): 
            if seats[i] == '1' and seats[j] == '1': 
                min_dist = min(min_dist,abs(i-j)) 
    return min_dist
     
for i in range(N): 
    for j in range(i+1,N): 
        if seats[i] == '0' and seats[j] == '0': 
            seats[i], seats[j] = '1', '1' 
            min_dist = count(seats) 
            ans = max(ans,min_dist)
            seats[i],seats[j] = '0','0'
print(ans)