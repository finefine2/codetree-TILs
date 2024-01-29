n, m = map(int, input().split())

arr = []
for i in range(n):
    st = list(map(int, input().split()))
    arr.append(st)

ans = 0
for i in range(n):
    cnt = 1
    for j in range(1, n):
        if arr[i][j] == arr[i][j-1]:
            cnt += 1
            if cnt >= m:
                ans += 1
                break     
        else:
            cnt = 1
        # if cnt >= m:
        #     ans += 1
        
for i in range(n):
    cnt = 1
    for j in range(1, n):
        if arr[j][i] == arr[j-1][i]:
            cnt += 1
            if cnt >= m:
                ans += 1
                break  
        else:
            cnt = 1
        # if cnt >= m:
        #     ans += 1

print(ans)