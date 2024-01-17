n = int(input())

# 전체 길이에서 한 선분만 뺐을때 그 선분 만큼의 길이가 안 줄어들면 겹치는 것
# 즉 한 선분만 뺄 경우 그 선분만큼 길이가 줄어들면 된다.
# -> 아니었다. 그냥 x1가 더 큰데, x2가 더 작은 것이 있을 경우 겹치게 되는 것!

s = 0
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
    s += abs(b - a)

ans = 0
for i in range(n):
    check = False
    for j in range(n):
        if i == j:
            continue
        
        if (arr[i][0] <= arr[j][0] and arr[i][1] >= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]):
            check = True
            break
    if not check:
        ans += 1

print(ans)