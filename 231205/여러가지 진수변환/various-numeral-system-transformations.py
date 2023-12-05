N, B = map(int,input().split()) 
ans = []
while True: 

    if N < B:
        ans.append(N)
        break 
    ans.append(N % B) 
    N //= B 

for a in ans[::-1]: 
    print(a,end="")