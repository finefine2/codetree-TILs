from functools import cmp_to_key
n = int(input())

def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    if str(x) + str(y) < str(y) + str(x):
        return 1
    
    return 0

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

arr.sort(key = cmp_to_key(compare))

for k in arr:
    print(k, end = "")