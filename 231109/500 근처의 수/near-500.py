nums = list(map(int,input().split())) 

max1, min2 = 0, 2000
for n in nums: 

    if n < 500 and n > max1: 
        max1 = n 
    
    elif n > 500 and n < min2: 
        min2 = n 
print(max1, min2)