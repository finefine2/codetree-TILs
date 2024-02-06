N = int(input()) 
scores = [] 
for _ in range(N): 
    c,s = input().split() 
    scores.append((c,int(s))) 
a,b,c = 0,0,0
'''
3 개 
3C3
a == b == c 
2 개 
3C2 
a == b and b != c 
a == c and a != b 
b == c and a != b

1 개 
3C1
a > b and a > c 
b > a and b > c 
c > a and c > b 
'''
def check_max(x,y,z): 
    # 3 개 같음
    if x == y and y == z and z == x: 
        return 1 
    # 2개 같음 
    elif x == y and x != z: 
        return 2 
    elif x == z and x != y: 
        return 3 
    elif y == z and y != x: 
        return 4 
    # 1개만 젤 큼 
    else: 
        return 5 
ans = [1] + [0] * N 
for i,s in enumerate(scores): 
    if s[0] == "A": 
        a += s[1]  
    elif s[0] == "B": 
        b += s[1] 
    elif s[0] == "C": 
        c += s[1] 
    winner = check_max(a,b,c) 
    ans[i+1] = winner 
cnt = 0 
for i in range(len(ans)-1): 
    if ans[i] != ans[i+1]: 
        cnt += 1 
print(cnt)