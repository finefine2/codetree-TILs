MAX_K = 100000
N = int(input()) 
a = [0] * (2 * MAX_K + 1) 
cnt_b = [0] * (2 * MAX_K + 1) 
cnt_w = [0] * (2 * MAX_K + 1) 

b,w,g = 0,0,0
cur = MAX_K

for _ in range(N): 
    x,c = input().split()
    x = int(x) 

    if c == "L":
        # go left 
        while x > 0: 
            a[cur] = 1 
            cnt_w[cur] += 1 
            x -= 1 
            if x: 
                cur -= 1 
    elif c == "R": 
        # go right 
        while x > 0: 
            a[cur] = 2
            cnt_b[cur] += 1 
            x -= 1 
            if x: 
                cur += 1
for i in range(2*MAX_K+1): 
    if cnt_b[i] >= 2 and cnt_w[i] >= 2: 
        g += 1
    elif a[i] == 1: 
        w += 1 
    elif a[i] == 2: 
        b += 1 
print(w, b, g)