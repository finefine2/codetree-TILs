# my solution 
# N = int(input()) 
# # 검은색은 -1 
# # 흰색은 1 
# OFFSET = 10000

# lines = [0] * 20001 

# start = OFFSET
# for _ in range(N): 
#     x, d = input().split() 
#     x = int(x) 
    
#     # left --> white. let it be 1
#     if d == "L": 
#         for i in range(start,start-x,-1): 
#             lines[i] = 1
#         start = start - x +1
#     # right --> black. let it be -1 
#     elif d == "R":
#         for i in range(start,start+x): 
#             lines[i] = -1
#         start = start + x -1

# ans1, ans2 = 0,0
# for l in lines:
#     if l == 1: 
#         ans1 += 1 
#     elif l == -1: 
#         ans2 += 1 
# print(ans1, ans2) 

# given solution 
MAX_K = 100000 

n = int(input()) 
a = [0] * (2 * MAX_K + 1) 
b,w = 0,0 

cur = MAX_K
for _ in range(n): 
    x,c = input().split() 
    x = int(x) 
    if c == 'L': 
        while x > 0: 
            a[cur] = 1 
            x -= 1 

            if x: 
                cur -= 1 
    else:
        while x > 0: 
            a[cur] = 2 
            x -= 1 

            if x: 
                cur += 1 
for i in range(2 * MAX_K + 1): 
    if a[i] == 1: 
        w += 1 
    elif a[i] == 2: 
        b += 1 
print(w,b)