n, k = map(int, input().split())

arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

# 바로 전 동전의 가치의 배수로 주어지므로 뒤에서 부터 큰 순서로 하면 될듯
ans = 0
for i in range(n-1, -1, -1):
    if k // arr[i] > 0:
        num = (k // arr[i])
        k -= (num * arr[i])
        ans += num

print(ans)