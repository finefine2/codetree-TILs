n = int(input())


arr = []
for i in range(n):
    c, s = map(str, input().split())
    arr.append((c, s))

aa, bb, cc = False, False, False
ab, bc, ca = False, False, False
abc = True

a, b, c = 0,0,0

ans = 0
for k in arr:
    if k[0] == 'A':
        a += int(k[1])
    elif k[0] == 'B':
        b += int(k[1])
    else:
        c += int(k[1])
    
    if a > b and a > c and not aa:
        ans += 1
        aa = True
        bb = False if bb else bb
        cc = False if cc else cc
        ab = False if ab else ab
        bc = False if bc else bc
        ca = False if ca else ca
        abc = False if abc else abc
    if b > a and b > c and not bb:
        ans += 1
        bb = True
        aa = False if aa else aa
        cc = False if cc else cc
        ab = False if ab else ab
        bc = False if bc else bc
        ca = False if ca else ca
        abc = False if abc else abc
    if c > a and c > b and not cc:
        ans += 1
        cc = True
        bb = False if bb else bb
        aa = False if aa else aa
        ab = False if ab else ab
        bc = False if bc else bc
        ca = False if ca else ca
        abc = False if abc else abc
    if a == b and a > c and not ab:
        ans += 1
        ab = True
        bb = False if bb else bb
        cc = False if cc else cc
        aa = False if aa else aa
        bc = False if bc else bc
        ca = False if ca else ca
        abc = False if abc else abc
    if b == c and b > a and not bc:
        ans += 1
        bc = True
        bb = False if bb else bb
        cc = False if cc else cc
        ab = False if ab else ab
        aa = False if aa else aa
        ca = False if ca else ca
        abc = False if abc else abc
    if c == a and c > b and not ca:
        ans += 1
        ca = True
        bb = False if bb else bb
        cc = False if cc else cc
        ab = False if ab else ab
        bc = False if bc else bc
        aa = False if aa else aa
        abc = False if abc else abc
    if a == b and b == c and not abc:
        ans += 1
        abc = True
        bb = False if bb else bb
        cc = False if cc else cc
        ab = False if ab else ab
        bc = False if bc else bc
        ca = False if ca else ca
        aa = False if aa else aa

print(ans)