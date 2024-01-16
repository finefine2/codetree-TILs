n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = 0
for i in range(n - m + 1):
    arr_s = sorted(arr[i:i+m])
    arr2_s = sorted(arr2)
    if arr_s == arr2_s:
        ans += 1

print(ans)

# 어차피 모든 경우의 수 이므로 내림차순 하면 같으니 이와 같은 방법 사용 가능