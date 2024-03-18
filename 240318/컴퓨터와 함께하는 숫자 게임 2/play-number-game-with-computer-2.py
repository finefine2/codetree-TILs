m = int(input())

a, b = map(int, input().split())

Min = m
Max = 0

def find(num):
    left = 1
    right = m
    cnt = 0

    while left <= right:
        mid = (left + right) // 2
        cnt += 1
        
        if mid > num:
            right = mid - 1
        elif mid < num:
            left = mid + 1
        else:
            return cnt

for k in range(a, b + 1):
    a = find(k)

    Min = min(Min, a)
    Max = max(Max, a)

print(Min, Max)