n = int(input())

arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            flag = False
            check = [0] * 110

            for l in range(n):
                if l == k or l == j or l == i:
                    continue
                
                for c in range(arr[l][0], arr[l][1] + 1):
                    check[c] += 1
                    
                # for a, b in arr[l]:
                #     for c in range(a, b+1):
                #         check[c] += 1
                
            for c in check:
                if c > 1:
                    flag = True
                
            if not flag:
                ans += 1

                

print(ans)