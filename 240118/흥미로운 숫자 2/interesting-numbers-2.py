x, y = map(int, input().split())

def inter(num):
    arr = list(str(num))
    arr.sort()
    if (arr.count(arr[0]) == 1 and arr.count(arr[1]) == len(arr) - 1) or (arr.count(arr[0]) == len(arr) - 1 and arr.count(arr[len(arr) - 1]) == 1):
        return True
    else:
        return False
        
ans = 0
for i in range(x, y+1):
    if inter(i):
        ans += 1

print(ans)