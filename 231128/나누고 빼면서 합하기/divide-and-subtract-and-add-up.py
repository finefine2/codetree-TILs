n,m = map(int,input().split()) 
A = list(map(int,input().split())) 
ans = 0
while True: 
    ans += A[int(m)-1]

    if m % 2 == 0: 
        m /= 2 
    elif m % 2 != 0: 
        m -= 1 

    if m == 1:
        break 
print(ans+A[0])