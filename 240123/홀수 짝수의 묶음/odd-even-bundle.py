n = int(input())

arr = list(map(int, input().split()))

odd = 0
even = 0
for k in arr:
    if k % 2 == 0:
        even += 1
    else:
        odd += 1

ans = 0
iseven = True
while True:
    if even <= 0 and odd <= 0:
        break

    if iseven:
        if even > 0:
            even -= 1
        else:
            if odd < 2:
                ans -= 1
                break
            
            odd -= 2
    else:
        if odd > 0:
            odd -= 1
        else:
            if even < 2:
                ans -= 1
                break
            
            even -= 2
    
    ans += 1
    iseven = not iseven

print(ans)


# 짝 = 짝 + 짝
#    = 홀 + 홀

# 홀 = 짝 + 홀
#    = 홀 + 짝