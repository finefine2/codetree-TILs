n = int(input())

arr = []
for i in range(n):
    a = int(input())
    arr.append(a)

ans = 0
for i in range(1000):
    cnt = 0
    flag = False
    for j in range(len(arr)):
        if arr[j] - i >= 0:
            if not flag:
                cnt += 1
            flag = True
        else:
            if flag:
                flag = False
    
    ans = max(ans, cnt)

print(ans)