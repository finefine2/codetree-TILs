N, T = map(int,input().split()) 

belt1 = list(map(int,input().split())) 
belt2 = list(map(int,input().split())) 
'''
1 2 3
6 5 1

1 1 2
3 6 5
'''
for _ in range(T): 
    tmp1 = belt1[-1] 
    tmp2 = belt2[-1] 

    for i in range(N-1,0,-1): 
        belt1[i] = belt1[i-1] 
        belt2[i] = belt2[i-1] 
    belt1[0] = tmp2 
    belt2[0] = tmp1 

for b in belt1: 
    print(b, end = " ") 
print() 
for b in belt2: 
    print(b,end = " ")