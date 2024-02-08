import math
n, m = map(int, input().split())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

def cal(x1, y1, x2, y2):
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
    

import sys
Min = sys.maxsize
select = []

def choose(num, select):
    global Min

    if len(select) == m:
        Max = 0
        for i in range(len(select)):
            for j in range(i+1, len(select)):
                Max = max(Max, cal(select[i][0], select[i][1], select[j][0], select[j][1]))

        Min = min(Min, Max)
        return 
    
    for i in range(num, n):
        choose(i+1, select + [arr[i]])

choose(0, [])
print(Min)