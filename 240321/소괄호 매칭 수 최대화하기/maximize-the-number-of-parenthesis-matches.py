from functools import cmp_to_key

n = int(input())


def compare(s1, s2):
    x1, y1 = s1
    x2, y2 = s2

    if x1 * y2 > x2 * y1:
        return -1
    if x1 * y2 == x2 * y1:
        return 0

    return 1

ans = 0
arr = []
for i in range(n):
    s = input()
    opens, close = 0, 0
    for c in s:
        if c == '(':
            opens += 1
        else:
            close += 1
        
            ans += opens
    
    arr.append((opens, close))

arr.sort(key=cmp_to_key(compare))
open_num = 0
for opens, close in arr:
    ans += open_num * close
    open_num += opens

print(ans)