n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))


# def is_subsequence(a, b, n, m):
#     i = 0  
#     j = 0  

#     # A와 B를 순회하며 B의 모든 요소가 A에 순서대로 있는지 확인
#     while i < n and j < m:
#         if a[i] == b[j]:
#             j += 1
#         i += 1

#     # B의 모든 요소가 A에서 찾아졌는지 여부를 반환
#     return j == m

# ans = 0

# for k in range(len(b)):
#     c = b[:k] + b[k+1:]

#     if is_subsequence(a, c, n, m-1):
#         ans += 1

# print(ans)

L = [0] * (m + 2)
R = [0] * (m + 2)

i = 1
for j in range(1, m + 1):
    while i <= n and a[i] != b[j]:
        i += 1
    L[j] = i
    if i <= n:
        i += 1

i = n
for j in range(m, 0, -1):
    while i >= 1 and a[i] != b[j]:
        i -= 1
    R[j] = i
    if i >= 1:
        i -= 1

L[0] = 0
R[m + 1] = n + 1

ans = 0
for j in range(1, m+1):
    if L[j - 1] < R[j + 1]:
        ans += 1
    # 검사를 할 때 L과 R을 따로 만들어서 가운데인 j만 빼고 검사하면 됨

print(ans)