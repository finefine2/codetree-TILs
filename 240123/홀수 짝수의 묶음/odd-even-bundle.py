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

    if iseven:   # 짝수를 만들때
        # 짝수가 있을 경우 짝수만 사용
        if even > 0:
            even -= 1
        else:     # 짝수를 만들어야 하는데 짝수도 없고, 홀수도 1개 이하 있을 경우 
                  # 불가능 하므로 이 홀수들을 앞의 홀수 만들때나 짝수만들때 넣어주고 ans를 하나 줄인다.
            if odd < 2:
                ans -= 1
                break
            
            odd -= 2
    else: # 홀수를 만들때 odd가 없으면 짝수로는 홀수를 만들 수 없음
        if odd == 0:
            break
            
        # 그냥 홀수를 만들때는 odd 한개로도 가능
        odd -= 1
    
    ans += 1
    iseven = not iseven

print(ans)


# 짝 = 짝 + 짝
#    = 홀 + 홀

# 홀 = 짝 + 홀
#    = 홀 + 짝