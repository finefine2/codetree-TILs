N,T = map(int,input().split()) 

first = list(map(int,input().split())) 
second = list(map(int,input().split())) 
third = list(map(int,input().split())) 
'''
1 2 4 
5 9 3 
6 5 1 

1 1 2
4 5 9 
3 6 5
'''

def move(): 
    tmp1, tmp2, tmp3 = first[-1],second[-1],third[-1] 
    for i in range(N-1,0,-1): 
        first[i] = first[i-1] 
        second[i] = second[i-1] 
        third[i] = third[i-1] 
    second[0], third[0], first[0] = tmp1, tmp2, tmp3 

for _ in range(T): 
    move() 

for f in first:
    print(f,end=" ") 
print()
for s in second: 
    print(s,end=" ")
print()
for t in third: 
    print(t,end=" ")