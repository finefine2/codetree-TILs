nums = list(map(int,input().split())) 

cand = []
for n in nums: 
    if n == 999 or n == -999: 
        break 
    cand.append(n) 
print(max(cand), min(cand))