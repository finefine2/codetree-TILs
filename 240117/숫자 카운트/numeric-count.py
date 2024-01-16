n = int(input())

ans = 0

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            
            check = True
            for a, b, c in arr:
                x = a // 100
                y = (a // 10) % 10
                z = a % 10

                one = 0
                two = 0

                if x == i:
                    one += 1
                if y == j:
                    one += 1
                if z == k:
                    one += 1
                if x == j or x == k:
                    two += 1
                if y == i or y == k:
                    two += 1
                if z == i or z == j:
                    two += 1

                if one != b or two != c:
                    check = False
                    break
            if check:
                ans += 1
                
    
print(ans)

# 1번 : 숫자 중 하나가 동일한 자리에 있을 경우 1번 카운트
# 2번 : 숫자 중 하나가 있긴 하나 다른 자리에 위치