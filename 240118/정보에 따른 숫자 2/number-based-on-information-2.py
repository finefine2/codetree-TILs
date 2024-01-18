T, a, b = map(int,input().split()) 
pos = [] 
for _ in range(T): 
    c,x = input().split()
    pos.append([c,int(x)]) 

# 매 위치를 갱신하면서 체크하기 
def check_dist(pos,num): 
    dist1 = 10000 
    dist2 = 10000
    for c,x in pos: 
        if c == "S": 
            dist1 = min(dist1, abs(num-x))
        elif c == "N": 
            dist2 = min(dist2, abs(num-x)) 
    if dist1 <= dist2: 
        return True 
ans = 0 
for i in range(a,b+1): 
    if check_dist(pos,i):
        ans += 1 
print(ans)