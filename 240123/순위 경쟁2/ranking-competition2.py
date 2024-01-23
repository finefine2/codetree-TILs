n = int(input())

arr = []
for i in range(n):
    c, s = map(str, input().split())
    arr.append((c, s))

a, b = 0, 0
aa = False
bb = False
both = True

ans = 0
for k in arr:
    
    if k[0] == 'A':
        a += int(k[1])
    else:
        b += int(k[1])
    
    if a == b and not both:
        ans += 1
        both = True
        if aa:
            aa = False
        if bb:
            bb = False
    if a > b and not aa:
        ans += 1
        aa = True
        if bb:
            bb = False
        if both:
            both = False
    if a < b and not bb:
        ans += 1
        bb = True
        if aa:
            aa = False
        if both:
            both = False

print(ans)