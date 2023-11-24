def count(n): 
    mid = 0 
    for i in range(1,n+1): 
        mid += i 
    return mid // 10 

n = int(input())
print(count(n))