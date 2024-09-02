N,T = tuple(map(int,input().split())) 
first = list(map(int,input().split())) 
second = list(map(int,input().split())) 

for _ in range(T): 
    temp = first[N-1] 
    for i in range(N-1,0,-1): 
        first[i] = first[i-1] 
    first[0] = second[N-1] 

    for i in range(N-1,0,-1): 
        second[i] = second[i-1] 
    second[0] = temp 
for elem in first: 
    print(elem,end=" ") 
print() 
for elem in second: 
    print(elem,end=" ")