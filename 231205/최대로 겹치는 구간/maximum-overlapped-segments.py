'''
지점이 겹치는지가 궁금할 때에는 x1부터 x2까지 
구간이 겹치는지가 궁금할 때에는 x1부터 x2-1까지 
'''

n = int(input()) 
lines = [0] * 201

offset = 100 
for _ in range(n): 
    x1, x2 = map(int,input().split()) 
    x1 += offset
    x2 += offset
    for i in range(x1,x2): 
        lines[i] += 1

print(max(lines) )