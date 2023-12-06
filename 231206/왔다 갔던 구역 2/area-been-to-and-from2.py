# lines = [0] * 10000
# start = 5000
# N = int(input()) 

# for _ in range(N): 
#     x,d = input().split()
#     x = int(x) 
#     if d == "R": 
#         for i in range(start,start+x+1): 
#             lines[i] += 1
#         start = start + x
#     elif d == "L": 
#         for i in range(start,start-x-1,-1):
#             lines[i] += 1
#         start = start - x 
# cnt = [] 
# for i in range(len(lines)): 
#     if lines[i] >= 2: 
#         cnt.append(i) 
# ans = 0 

# for i in range(len(cnt)-1): 
#     if cnt[i+1] - cnt[i] == 1:
#         ans += 1
# print(ans)
n = int(input())

arr = []

#현재 위치
loca = 0

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == 'R':
        right = loca + a
        left = loca
        loca += a
            
    elif b == 'L':
        left = loca - a
        right = loca
        loca -= a

    arr.append([left, right])

check = [0] * 101

for x1, x2 in arr:
    for i in range(x1, x2):
        check[i] += 1

cnt = 0
for i in check:
    if i >= 2:
        cnt += 1
print(cnt)