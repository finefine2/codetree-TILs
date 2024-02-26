n = int(input())

arr = list(map(int, input().split()))

flag = False

if sum(arr) % 4:
    flag = True
    print(0)
    quit()

s = sum(arr) // 4

L = [0] * (n+1)
R = [0] * (n+1)

num = arr[0]
cnt = 0
if num == s:
    cnt = 1
# arr[0] 이 이미 s일 경우 cnt는 1

for i in range(1, n):
    num += arr[i]

    # num에 arr을 더해주다가 이 값이 2*s 가 될 경우 L에 cnt를 넣어준다.
    # 두개의 구간을 만들 수 있는 가능성이 있으므로 기록
    if num == 2 * s:
        L[i] = cnt
    
    # num이 s가 될 경우에는 cnt를 증가시켜준다.
    if num == s:
        cnt += 1

# 즉, 여기에서만든 L은 0번부터 i번까지 합이 s인 구간을 정확하게 2개 만들 수 있는 가지수이다.

R[n-1] = 0
num = arr[n-1]
cnt = 0
if num == s:
    cnt = 1

for i in range(n-2, -1, -1):
    num += arr[i]

    if num == 2 * s:
        R[i] = cnt
    
    if num == s:
        cnt += 1

ans = 0

for i in range(1, n-1):
    ans += L[i] * R[i + 1]

# 그러니까 [0, i]와 [i+1, n-1]에 정확히 2개의 구간이 놓이기 위한 가지수가
# L[i] * R[i+1]이다.

# [0, i] 까지의 합이 s인 구간을 정확히 2개 만들고
# [i+1, n] 까지도 합이 s인 구간을 정확히 2개 만들어서 경우의 수를 구하기 위해 곱해준다.

print(ans)