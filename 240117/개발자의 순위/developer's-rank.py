k, n = map(int, input().split())

arr = [[0] * 20 for _ in range(20)]
for i in range(k):
    tmp = list(map(int, input().split()))
    for i in range(len(tmp)):
        for j in range(i+1, len(tmp)):
            arr[tmp[i]-1][tmp[j]-1] = 1

ans = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and arr[j][i] != 1:
            ans += 1

print(ans)

# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end = " ")
#     print()

# 4 1
# 4 2
# 4 3
# 1 2
# 1 3
# 2 3