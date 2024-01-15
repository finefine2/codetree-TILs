n,m,d,s=map(int,input().split()) # 사람, 치즈, 치즈 먹은 수, 아픈 기록 수
MAX_T=100

array=[[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(MAX_T+1)]
for i in range(d):
    p,em,t=map(int,input().split()) # 몇번쨰 사람이 몇번째 치즈를 언제 먹었는지 (p,m,t)
    array[t][p][em]=1

cheese=[0 for _ in range(m+1)]
for i in range(s):
    p,t=map(int,input().split())
    for k in range(t-1,0,-1): # 시간
        for j in range(1,m+1):
            if array[k][p][j]:
                cheese[j]+=1   
stale=[]
for i in range(1,m+1):
    if cheese[i]>=s:
        stale.append(i)

people=set()
for i in range(1,MAX_T+1): # 시간
    for j in range(1,n+1): # 사람
        for k in stale: 
            if array[i][j][k]:
                people.add(j)
print(len(people))