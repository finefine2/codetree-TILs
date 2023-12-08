n,m = map(int,input().split()) 

OFFSET = 100 

A = [0] * OFFSET
B = [0] * OFFSET

'''
idx  0 1 2 3 4 5 6 7 8 9 10 11 12 13
A    0 1 2 3 4 5 6 7 8 9 8  7  6  7
'''
# A
startA = 0
cntA = 0
for _ in range(n): 
    d,t = input().split() 
    t = int(t) 

    if d == "R": 
        for i in range(startA,startA+t):
            A[cntA] = i 
            cntA += 1 
        startA = startA + t 
    elif d == "L":
        for i in range(startA,startA-t,-1): 
            A[cntA] = i 
            cntA += 1 
        startA = startA - t

startB = 0 
cntB = 0 
for _ in range(m): 
    d,t = input().split() 
    t = int(t) 
    if d == "R": 
        for i in range(startB,startB+t): 
            B[cntB] = i 
            cntB += 1 
        startB = startB + t 
    elif d == "L": 
        for i in range(startB,startB-t,-1): 
            B[cntB] = i 
            cntB += 1 
        startB = startB -t 
ans = -1 

length = min(len(A),len(B))
for t in range(1,length+1): 
    if A[t] == B[t]: 
        ans = t
        break 
print(ans)