n = int(input())

arr = []
for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    
ans = 0
check = [0] * (n+1)
def choose(row, total):
    global ans
    if row == n:
        ans = max(ans, total)
        return
    
    for col in range(n):
        if not check[col]:
            check[col] = 1
            choose(row + 1, total + arr[row][col])
            check[col] = 0


choose(0, 0)
print(ans)